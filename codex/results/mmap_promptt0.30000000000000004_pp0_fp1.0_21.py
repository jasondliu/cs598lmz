import mmap
# Test mmap.mmap(-1, 0)
with open('/dev/zero', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'abcd')
    m.seek(0)
    assert m.read(4) == b'abcd'
    m.close()

# Test mmap.mmap(fd, 0)
with open('/dev/zero', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'abcd')
    m.seek(0)
    assert m.read(4) == b'abcd'
    m.close()

# Test mmap.mmap(fd, 0, access=ACCESS_READ)
with open('/dev/zero', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, mmap.ACCESS_READ)
    m.write(b'abcd')
    m.seek(0)
    assert m.read
