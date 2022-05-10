import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.tell())
    m.write(b'foo')
    print(m.tell())
    print(m.tell(), file=f)
