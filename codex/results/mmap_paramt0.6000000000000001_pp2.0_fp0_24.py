import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    assert m.read(1) == bytes(2)
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(3)[0]
    m.seek(0)
    assert m.read(1) == bytes(3)
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(4)
    m.seek(0)
    assert m.read(1) == bytes(4)
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(bytes(5)[0])
    m.seek(0)
    assert m.read(1) == bytes(5)
    m.close
