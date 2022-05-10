import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    assert m[0] == 1
    m[0] = 2
    m.flush()
    m.close()

with open('test', 'rb') as f:
    assert f.read() == bytes([2])
