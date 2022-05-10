import mmap
# Test mmap.mmap(0, 1)
m = mmap.mmap(-1, 1)
m.close()

# Test mmap.mmap(0, 1, mmap.MAP_PRIVATE)
m = mmap.mmap(-1, 1, mmap.MAP_PRIVATE)
m.close()

# Test mmap.mmap(0, 1, mmap.MAP_SHARED)
m = mmap.mmap(-1, 1, mmap.MAP_SHARED)
m.close()

# Test mmap.mmap(0, 1, mmap.MAP_SHARED, mmap.PROT_READ)
m = mmap.mmap(-1, 1, mmap.MAP_SHARED, mmap.PROT_READ)
m.close()

# Test mmap.mmap(-1, 1, mmap.MAP_SHARED, mmap.PROT_READ, None)
m = mmap.mmap(-1, 1, mmap.MAP_SHARED, mmap.PROT_READ)
