import mmap
# Test mmap.mmap()

def test_mmap():
    mm = mmap.mmap(-1, 1024)
    mm.write(b'0123456789')
    assert mm.read(5) == b'01234'
    assert mm.read(5) == b'56789'
    mm.seek(0)
    assert mm.read(5) == b'01234'
    assert mm.read(5) == b'56789'
    mm.close()

def test_mmap_write():
    mm = mmap.mmap(-1, 1024)
    mm.write(b'0123456789')
    mm.seek(0)
    mm.write(b'abcdefghij')
    mm.seek(0)
    assert mm.read(5) == b'abcde'
    assert mm.read(5) == b'fghij'
    mm.close()

def test_mmap_write_overflow():
    mm = mmap.mmap(-1, 1024)
    mm.write(b'012345
