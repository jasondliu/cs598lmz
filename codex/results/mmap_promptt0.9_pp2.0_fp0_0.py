import mmap
# Test mmap.mmap(-1, prot=mmap.ACCESS_WRITE) behavior on supported plaforms.
with open('/dev/zero', 'r+b') as f:
    m = mmap.mmap(-1, mmap.PAGESIZE*4, prot=mmap.ACCESS_WRITE, fileno=f.fileno())
    # The -1 size is ignored.
    assert len(m) == mmap.PAGESIZE*4
    # Bad file descriptor is ignored.
    m = mmap.mmap(-1, mmap.PAGESIZE*4, prot=mmap.ACCESS_WRITE, fileno=-1)
    assert len(m) == mmap.PAGESIZE*4
    # Negative len is a ValueError.
    m = mmap.mmap(-1, mmap.PAGESIZE*4, prot=mmap.ACCESS_WRITE)
    m.close()
    with pytest.raises(ValueError):
        mmap.mmap(-1, -1, prot=mmap.ACCESS_WRITE)

# Test on
