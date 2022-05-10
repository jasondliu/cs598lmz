import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = b'\x00'
</code>
It works fine and the file is correctly truncated.
But if I open the file with <code>os.open</code> and <code>mmap.mmap</code> like this:
<code>import mmap
import os

with open('test', 'wb') as f:
    f.write(bytes(1))

fd = os.open('test', os.O_RDWR)
m = mmap.mmap(fd, 0)
m[0:1] = b'\x00'
os.close(fd)
</code>
It does not work and the file is not truncated.
What is my mistake ?

