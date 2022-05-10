import mmap
# Test mmap.mmap.read for readonly maps
f = open(test.testdir + "/core.mem", "rb")
mf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
c = mf.read(len("\n"))
print("len is %d, c is %s" % (len(c), c))
mf.close()
f.close()
# Test mmap.mmap.read for readwrite maps
f = open(test.testdir + "/core.mem", "rb+")
mf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
c = mf.read(len("\n"))
print("len is %d, c is %s" % (len(c), c))
mf.close()
f.close()
# Test mmap.mmap.read for private maps
f = open(test.testdir + "/core.mem", "rb+")
