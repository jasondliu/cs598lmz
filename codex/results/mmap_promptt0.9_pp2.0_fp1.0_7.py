import mmap
# Test mmap.mmap() with read-only buffer.  On Windows, allow buffer to be
# larger than file can grow to.
with open('data', 'w+') as f:
    f.write('Five rings for the five dwarves. The rings were their mother's.\n')
    f.seek(0)
    m = mmap.mmap(f.fileno(), 10, access=mmap.ACCESS_READ)
    print '1st 10 bytes via slice:', `m[:10]`
    print '1st 10 bytes via buffer:', repr(m[:10])
    del m
