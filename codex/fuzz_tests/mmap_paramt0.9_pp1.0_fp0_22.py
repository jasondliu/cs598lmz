import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    mfile = mmap.mmap(-1, 0, mmap.MAP_PRIVATE, mmap.PROT_READ | mmap.PROT_WRITE, m, 0)
    mfile.move(0, 10)
</code>
Example 2:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    mfile = mmap.mmap(-1, 0, mmap.MAP_PRIVATE, mmap.PROT_READ | mmap.PROT_WRITE, m, 0)
    mfile[0] = b'1'
</code>
Example 3:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

