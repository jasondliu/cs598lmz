import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(3)
    print(m.read(1))
    print(m.read(1))
    print(m.read(1))
    m[:1] = b'\x02'
    m[1:2] = b'\x03'
    m[2:3] = b'\x04'
