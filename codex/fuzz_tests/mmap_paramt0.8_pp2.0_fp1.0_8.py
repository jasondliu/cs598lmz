import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), offset=0, length=1)
    for i in range(1, 100):
        m.seek(0)
        m.write(bytes(i))
        m.flush()
</code>

