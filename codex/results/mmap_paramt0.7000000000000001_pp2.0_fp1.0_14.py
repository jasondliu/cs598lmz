import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print('mmap  :', m[0], m[0] == 1)
    print('file  :', f.read(1), f.read(1) == '\x01')
    print('cached:', m[0], m[0] == 1)
    m[0:1] = b'\x00'
    print('mmap  :', m[0], m[0] == 0)
    print('file  :', f.read(1), f.read(1) == '\x01')
    print('cached:', m[0], m[0] == 0)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    print('mmap  :', m.read(1), m.read(1) == '\x00')
    print('file  :', f.read(1), f.read(1) == '\x00')
    print('cached:', m.read(1), m.
