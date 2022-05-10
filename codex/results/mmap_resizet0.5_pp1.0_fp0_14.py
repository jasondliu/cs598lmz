import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
How can I prevent the <code>ValueError</code>?


A:

The solution is to use the <code>mmap.ACCESS_READ</code> flag and to unmap the memory map before truncating the file.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    a = m[:]
    m.close()
    f.truncate()
</code>

