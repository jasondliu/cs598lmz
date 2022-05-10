import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'abc')
</code>
It is not possible to write to a file opened in the <code>rb</code> mode.

