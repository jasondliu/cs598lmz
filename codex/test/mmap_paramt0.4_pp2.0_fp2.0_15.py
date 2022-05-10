import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
    m[0] = bytes(10)
    m[1] = bytes(10)
    m[2] = bytes(10)
    m[3] = bytes(10)
    m[4] = bytes(10)
    m[5] = bytes(10)
    m[6] = bytes(10)
    m[7] = bytes(10)
