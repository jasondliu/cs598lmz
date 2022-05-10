import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(b'XXX')
    m.seek(0)
    print(m.read(3))

with open('test', 'rb') as f:
    print(f.read())
