import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x00')
    m.write(b'\x01')
    m.write(b'\x02')
    m.write(b'\x03')
    m.write(b'\x04')
    m.write(b'\x05')
    m.write(b'\x06')
    m.write(b'\x07')
    m.write(b'\x08')
    m.write(b'\x09')
    m.write(b'\x0a')
    m.write(b'\x0b')
    m.write(b'\x0c')
    m.write(b'\x0d')
    m.write(b'\x0e')
    m.write(b'\x0f')
    m.write(b'\x10')
    m.write(b'\x11')
    m.write(b'\x12')
    m.write(b'\x13')
    m.write(b'
