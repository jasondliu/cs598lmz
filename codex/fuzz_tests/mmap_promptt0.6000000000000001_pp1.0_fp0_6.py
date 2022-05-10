import mmap
# Test mmap.mmap.write
f = open(test.test_support.TESTFN, "wb+")
f.write("a" * mmap.ALLOCATIONGRANULARITY)
f.flush()
m = mmap.mmap(f.fileno(), mmap.ALLOCATIONGRANULARITY, access=mmap.ACCESS_WRITE)
m.write("b" * mmap.ALLOCATIONGRANULARITY)
if m.read(mmap.ALLOCATIONGRANULARITY) != "b" * mmap.ALLOCATIONGRANULARITY:
    raise TestFailed("write() didn't change the mmap'ed data")
m.close()
f.close()

# Test mmap.mmap.read_byte
f = open(test.test_support.TESTFN, "wb+")
f.write("a" * mmap.ALLOCATIONGRANULARITY)
f.flush()
m = mmap.mmap(f.fileno(), mmap.ALLOCATIONGRANULARITY, access=mmap.ACCESS_READ)
if
