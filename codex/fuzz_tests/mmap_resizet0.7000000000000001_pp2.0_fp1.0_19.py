import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.flush()
    f.seek(0)
    f.write(bytes(10))
    f.flush()
    a = m[:]
