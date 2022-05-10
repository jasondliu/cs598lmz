import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an exception
<code>mmap.error: [Errno 9] Bad file descriptor
</code>
I'm on Linux, and I'm trying to find a way to resize an mmap file without having to unmap it and then map it again.


A:

You can use <code>mmap.resize</code>.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    mmap.resize(m, 0)
    a = m[:]
</code>

