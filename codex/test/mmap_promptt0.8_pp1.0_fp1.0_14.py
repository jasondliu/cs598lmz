import mmap
# Test mmap.mmap(0,1,prtot.PROT_READ) with a path that is not a filename.
m = mmap.mmap(0,1,prtot.PROT_READ|prtot.PROT_WRITE,mmap.MAP_SHARED,
              os.open("/dev/null",os.O_RDWR))
self.failUnlessEqual(m.readline(), None)
raise TestFailed("should have raised IOError")
