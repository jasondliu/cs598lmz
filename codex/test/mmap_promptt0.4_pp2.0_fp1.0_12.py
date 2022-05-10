import mmap
# Test mmap.mmap

def test_mmap():
    m = mmap.mmap(-1, 1024)
    m.write(b"Hello")
    m.seek(0)
    assert m.read(5) == b"Hello"
    m.close()

def test_mmap_readonly():
    m = mmap.mmap(-1, 1024)
    m.write(b"Hello")
    m.seek(0)
    assert m.read(5) == b"Hello"
    m.close()
    m = mmap.mmap(m.fileno(), 1024, access=mmap.ACCESS_READ)
    m.seek(0)
    assert m.read(5) == b"Hello"
    m.close()

def test_mmap_offset():
    m = mmap.mmap(-1, 1024)
    m.write(b"Hello")
    m.seek(0)
    assert m.read(5) == b"Hello"
    m.close()
