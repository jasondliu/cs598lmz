import mmap
# Test mmap.mmap.read() and mmap.mmap.read_byte()

with open('/dev/null', 'r+b') as f:
    s = f.read(10)
    assert s == b''
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    assert m.read(10) == b''
    assert m.read_byte() == b''
    assert m.read_byte() == b''
    m[10] = b'x'
    assert m.read(10) == b'x'
    assert m.read_byte() == b'x'
    assert m.read_byte() == b''
    assert m.readline() == b'x'
    m.close()

with open('/dev/null', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    assert m.read() == b''
    assert m.read() == b''
    m[10] = b
