import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 10)
    print(m[0])
    m[0] = b'c'

with open('test', 'r+b') as f:
    print(f.read(1))
    f.write(bytes(10))
