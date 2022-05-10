import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.move(1, 0, 3)
    m.close()

with open('test', 'rb') as f:
    assert f.read() == b'\x01\x00\x00'
