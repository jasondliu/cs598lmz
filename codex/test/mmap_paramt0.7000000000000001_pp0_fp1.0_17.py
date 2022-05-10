import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes([65])

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read()[0])

with open('test', 'w') as f:
    f.write('a')

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes([65])

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read()[0])

