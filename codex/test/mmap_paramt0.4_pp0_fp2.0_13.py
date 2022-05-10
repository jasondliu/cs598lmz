import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m[0] = 0
    print(m)
    m[0] = 1
    print(m)
    m.flush()
    print(m)
