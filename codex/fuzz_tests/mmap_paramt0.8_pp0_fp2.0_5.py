import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    for i in range(10):
        if i % 2 == 0:
            m.write(b'a')
        else:
            m.write(b'b')
    m.seek(0)
    print(m.read(10))
