import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes('1', 'ascii')
    m.close()
</code>
It's a good idea to use a context manager (the <code>with</code> statement) to ensure the file is closed and the mmap is unmapped.

