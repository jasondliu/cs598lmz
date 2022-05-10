import mmap
# Test mmap.mmap with an offset after a page boundary
with open(TESTFN, 'wb') as f:
    f.write(b'a' * mmap.PAGESIZE + b'b' * mmap.PAGESIZE)
with open(TESTFN, 'rb') as f:
    for offset in [0, mmap.PAGESIZE - 1, mmap.PAGESIZE, mmap.PAGESIZE + 1]:
        m = mmap.mmap(f.fileno(), mmap.PAGESIZE, offset=offset)
        m[:]
# check mmap.access
with open(TESTFN, 'rb') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        try:
            m[:] = b'abc'
        except TypeError as err:
            assert err.args[0] == 'Cannot modify read-only memory'
        assert m[:] == open(TESTFN, 'rb').read()
# Create a file with a block of all zeroes, and check that
