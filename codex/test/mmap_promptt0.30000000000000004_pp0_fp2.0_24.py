import mmap
# Test mmap.mmap(0, 1)
# This is a test for http://bugs.jython.org/issue2355
with open(support.TESTFN, 'wb') as f:
    f.write(b'\0')
with open(support.TESTFN, 'rb') as f:
    m = mmap.mmap(f.fileno(), 1)
    m.close()
with open(support.TESTFN, 'rb') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_READ)
    m.close()
with open(support.TESTFN, 'rb') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
    m.close()
with open(support.TESTFN, 'rb') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_COPY)
    m.close()
# Test mmap.mmap(-1, 1)
