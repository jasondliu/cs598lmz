import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(1, m[0])
    m[0] = b'A'
    m.flush()
    print(2, m[0])
    print(3, f.read(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(4, m[:])
    m[:] = b'B'
    m.flush()
    print(5, m[:])
    print(6, f.read())

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(7, m[:])
    m.write(b'C')
    m.flush()
    print(8, m[:])
    print(9, f.read())

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(10, m[:])
    m[:] = b
