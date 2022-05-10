import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.size())
    print(m.read())
    print(m.read(2))
    print(m.readline())
    print(m.read(2))
    print(m.read())
    m.close()
