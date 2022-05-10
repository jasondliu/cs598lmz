import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(bytes(1))
    m.write_byte(bytes(2))
    m.write_byte(bytes(3))
    m.write_byte(bytes(4))
    m.flush()

