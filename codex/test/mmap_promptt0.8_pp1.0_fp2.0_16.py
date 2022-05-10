import mmap
# Test mmap.mmap(0,1)
for i in xrange(1,1024):
        s = mmap.mmap(0,i)
        assert s.size() == i
        del s
