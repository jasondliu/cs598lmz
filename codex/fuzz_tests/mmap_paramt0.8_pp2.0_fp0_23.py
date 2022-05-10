import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
    bytes(m)
    m[0] = 2
    assert m[0] == 2
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    bytes(m)
    m[0] = 2
    assert m[0] == 1
    m[0] = 2
    m.close()

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    bytes(m)
    assert m[0] == 2
    # The following is probably implementation specific, but doesn't
    # hurt to test.
    with pytest.raises(TypeError):
        m[0] = 2
    m.close()

# This is not really very useful, but it's a funny case.
with open('test', 'rb') as f:
    m
