import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 20000, offset=1000, access=mmap.ACCESS_WRITE)
    print(m)
    m.resize(2000000)
    print(m)
