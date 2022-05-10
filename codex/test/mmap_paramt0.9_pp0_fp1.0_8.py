import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(bytes(1890))
    m.write(bytes(100))
    m.seek(0)
    out = m.read(20)
    print(out)
