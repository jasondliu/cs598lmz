import mmap
# Test mmap.mmap()
m = mmap.mmap(-1, 1)
# Test mmap.mmap()
m = mmap.mmap(-1, 1, access=mmap.ACCESS_READ)
# Test mmap.mmap()
m = mmap.mmap(-1, 1, prot=mmap.PROT_READ)
# Test mmap.mmap()
m = mmap.mmap(-1, 1, flags=mmap.MAP_SHARED)
# Test mmap.mmap()
m = mmap.mmap(-1, 1, offset=0)
# Test mmap.mmap()
m = mmap.mmap(-1, 1, fileno=0)
# Test mmap.mmap()
m = mmap.mmap(-1, 1, fileno=0, access=mmap.ACCESS_READ)
# Test mmap.mmap()
m = mmap.mmap(-1, 1, fileno=0, prot=mmap.PROT_READ)
# Test mmap.mmap()
m = mmap.mmap
