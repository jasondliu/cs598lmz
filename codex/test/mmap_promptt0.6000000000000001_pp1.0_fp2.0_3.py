import mmap
# Test mmap.mmap(-1,1)

with mmap.mmap(-1,1) as m:
    m.write(b'a')
    assert m[0] == b'a'
    m.seek(0)
    assert m.read(1) == b'a'

# Test mmap.mmap(0,1)

with mmap.mmap(0,1) as m:
    m.write(b'b')
    assert m[0] == b'b'
    m.seek(0)
    assert m.read(1) == b'b'

# Test mmap.mmap(1,1)

with mmap.mmap(1,1) as m:
    m.write(b'c')
    assert m[0] == b'c'
    m.seek(0)
    assert m.read(1) == b'c'

# Test mmap.mmap(2,1)

with mmap.mmap(2,1) as m:
    m.write(b'd')
