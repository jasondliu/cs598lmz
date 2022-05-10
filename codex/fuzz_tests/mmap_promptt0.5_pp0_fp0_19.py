import mmap
# Test mmap.mmap(0, 1)
m = mmap.mmap(-1, 1)
m[0] = '\0'
m.close()

# Test mmap.mmap(0, 1, mmap.MAP_PRIVATE)
m = mmap.mmap(-1, 1, mmap.MAP_PRIVATE)
m[0] = '\0'
m.close()

# Test mmap.mmap(0, 1, mmap.MAP_SHARED)
m = mmap.mmap(-1, 1, mmap.MAP_SHARED)
m[0] = '\0'
m.close()

# Test mmap.mmap(0, 1, mmap.MAP_SHARED, mmap.PROT_READ)
m = mmap.mmap(-1, 1, mmap.MAP_SHARED, mmap.PROT_READ)
m[0] = '\0'
m.close()

# Test mmap.mmap(0, 1, mmap.MAP_SHARED, mmap.
