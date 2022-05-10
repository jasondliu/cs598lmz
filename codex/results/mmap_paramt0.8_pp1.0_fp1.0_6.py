import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read_byte())  # 1
    m.write_byte(b'y')
    m.seek(0)
    print(m.read_byte())  # 121
    m.close()
