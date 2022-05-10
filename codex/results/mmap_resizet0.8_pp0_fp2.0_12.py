import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # return empty bytes
</code>
But it works fine if I create file with <code>os.open</code>:
<code>import os
import mmap

fd = os.open('test', os.O_CREAT | os.O_RDWR)
os.write(fd, bytes(1))
os.close(fd)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # return b'\x01'
</code>
What is the matter?


A:

I think that <code>mmap</code> expects the buffer to be physically contiguous. File mapping is virtual, so there is no guarantee that a buffer is contiguous.
In your first example, you <code>truncate</code> immediately after creating the file. This means that the OS will allocate a new (zero-length) buffer to store the file.
In your second example, the initial <code>write</code> causes the OS to allocate a buffer to store the file. When you
