import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read())
    print(m.size())
    print(m.tell())
    print(m.readline())
    m.seek(0)
    print(m.readline())
    print(m.read_byte())
    m.write_byte(bytes(2))
