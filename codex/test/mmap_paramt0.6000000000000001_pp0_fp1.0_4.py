import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = 49
    print(m[0])
    print(m[0:1])
    m[0:1] = b'\xff'
    print(m[0])
    print(m[0:1])
    print(m[0:1][0])
    print(m[0:1][0] == b'\xff')
    m[0] = 49
    print(m[0])
    print(m[0:1])
    print(m[0:1][0])
    print(m[0:1][0] == b'\xff')
    m[0:1] = b'\xff'
    print(m[0])
    print(m[0:1])
