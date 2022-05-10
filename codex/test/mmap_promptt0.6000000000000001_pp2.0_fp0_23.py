import mmap
# Test mmap.mmap() and mmap.mmap(-1, ...)
for f in [
        tempfile.TemporaryFile(),
        tempfile.TemporaryFile(mode='w+b'),
        tempfile.TemporaryFile(mode='w+t'),
        open(test.support.TESTFN, 'w+b'),
        open(test.support.TESTFN, 'w+t'),
        StringIO('x' * 10),
        StringIO('x' * 10),
        StringIO('x' * 10),
        BytesIO(b'x' * 10),
        BytesIO(b'x' * 10),
        BytesIO(b'x' * 10)
    ]:
    for start in range(-1, 3):
        for size in range(-1, 10):
            m = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_WRITE, offset=start)
            m[:] = b'x' * len(m)
            m.close()
            f.seek(0)
