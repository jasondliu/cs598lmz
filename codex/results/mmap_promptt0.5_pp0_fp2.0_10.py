import mmap
# Test mmap.mmap(fileno, length, access=ACCESS_READ, offset=0)
with open('/tmp/test_mmap', 'w+b') as f:
    f.write(b'\x00' * 100)
    f.flush()
    m = mmap.mmap(f.fileno(), 100, mmap.ACCESS_WRITE, offset=0)
    m[0] = b'\x01'
    m.close()
    f.seek(0)
    assert f.read(1) == b'\x01'
    f.close()

# Test mmap.mmap(fileno, length, access=ACCESS_WRITE, offset=0)
with open('/tmp/test_mmap', 'r+b') as f:
    f.write(b'\x00' * 100)
    f.flush()
    m = mmap.mmap(f.fileno(), 100, mmap.ACCESS_READ, offset=0)
    assert m[0] == b'\x00'
    m.close()

