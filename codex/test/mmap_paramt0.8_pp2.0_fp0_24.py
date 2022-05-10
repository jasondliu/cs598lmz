import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m)

    print(m.write(bytes(1)))

    m.seek(0)
    print(m.read())

    m.seek(0)
    m[0:0] = bytes(1)
    m.seek(0)
