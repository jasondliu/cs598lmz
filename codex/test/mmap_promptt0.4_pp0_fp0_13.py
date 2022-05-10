import mmap
# Test mmap.mmap
#m = mmap.mmap(0, 1024*1024, "MySharedMemory", mmap.ACCESS_READ)
#print m[:10]
#m.close()

# Test mmap.mmap(fileno)
#f = open("/dev/zero", "r+b")
#m = mmap.mmap(f.fileno(), 1024*1024)
#print m[:10]
#m.close()
#f.close()

# Test mmap.mmap(fileno, length)
#f = open("/dev/zero", "r+b")
#m = mmap.mmap(f.fileno(), 1024*1024, mmap.MAP_SHARED, mmap.PROT_READ)
#print m[:10]
#m.close()
#f.close()

# Test mmap.mmap(fileno, length, prot)
#f = open("/dev/zero", "r+b")
#m = mmap.mmap(f.fileno(), 1024*1024, mmap.MAP
