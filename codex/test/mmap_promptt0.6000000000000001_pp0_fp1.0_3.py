import mmap
# Test mmap.mmap

def test_mmap():
    m = mmap.mmap(-1,4096)
    m[0:5] = 'hello'
    assert m[0:5] == 'hello'
    assert len(m) == 4096
    assert m.size() == 4096
    m.close()

def test_mmap_write():
    m = mmap.mmap(-1,4096,access=mmap.ACCESS_WRITE)
    m[0:5] = 'hello'
    assert m[0:5] == 'hello'
    m.close()

def test_mmap_read():
    m = mmap.mmap(-1,4096,access=mmap.ACCESS_READ)
    raises(TypeError, "m[0:5] = 'hello'")
    m.close()

def test_mmap_error():
    raises(ValueError, "mmap.mmap(-1,4096,access=8)")

