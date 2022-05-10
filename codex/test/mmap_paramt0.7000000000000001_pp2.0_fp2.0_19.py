import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x1f\x8b\x08')
    m.seek(0)
    print(m.readline())
    print(m.readline())

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x1f\x8b\x08')
    m.seek(0)
    print(m.readline())
