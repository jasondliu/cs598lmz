import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(bytes(5))
    print(m.read(10))
    print(m.read(10))
    m.seek(0)
    print(m[0])
    print(m[1])
    m[1] = b'2'
    print(m[0])
    print(m[1])
    print(m.read(10))


import os

print(os.getcwd())
