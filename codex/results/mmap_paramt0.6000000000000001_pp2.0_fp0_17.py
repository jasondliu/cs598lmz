import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
</code>
Note that you can't <code>seek</code> and <code>write</code> in the same <code>mmap</code> instance.

