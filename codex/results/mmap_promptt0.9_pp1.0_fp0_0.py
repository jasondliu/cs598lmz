import mmap
# Test mmap.mmap() with file of size 0

with open(TESTFN, 'wb') as f:
    f.write(b'aaa')

with open(TESTFN, 'r+b') as f:
    # Test no-op resizing, but only when the underlaying file is
    # resizable (ie. open for write or create) otherwise it should
    # raise an error.
    try:
        mmap_f = mmap.mmap(f.fileno(), 0)
    except ValueError as e:
        # This platform does not support the 'whence' argument.
        assert "whence" in str(e)
    else:
        mmap_f.close()
    mmap_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    f.seek(0)
    f.write(b'bbb')
    assert mmap_f.read(3) == b'bbb'
    mmap_f.seek(0)
    mmap_f[0:3] = b
