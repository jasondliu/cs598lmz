import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(3)
    m.write_byte(bytes(1))
    m.write_byte(bytes(1))
    m.seek(0)
    print(m.read(3))
    m.close()
