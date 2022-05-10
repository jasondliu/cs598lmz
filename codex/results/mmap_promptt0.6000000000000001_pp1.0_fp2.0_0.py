import mmap
# Test mmap.mmap()
def test_mmap_mmap():
    with open('test.dat', 'w+b') as f:
        f.write(b"foobar")
        m = mmap.mmap(f.fileno(), 6)
        assert m[:] == b"foobar"

# Test mmap.mmap(fileno, 0)
def test_mmap_mmap_fileno_0():
    with open('test.dat', 'w+b') as f:
        f.write(b"foobar")
        f.flush()
        m = mmap.mmap(f.fileno(), 0)
        assert m[:] == b"foobar"

# Test mmap.mmap(-1, 0)
def test_mmap_mmap_fileno_negative_1():
    with open('test.dat', 'w+b') as f:
        f.write(b"foobar")
        f.flush()
        m = mmap.mmap(-1, 0)
        assert m[:] == b"foobar"

#
