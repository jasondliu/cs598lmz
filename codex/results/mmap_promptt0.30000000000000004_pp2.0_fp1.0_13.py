import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, 0, 0)
# Test mmap.mmap(0, 1, "shared", mmap.MAP_PRIVATE, 0, 0)
# Test mmap.mmap(-1, 1, "shared", mmap.MAP_SHARED, 0, 0)
# Test mmap.mmap(-1, 1, "shared", mmap.MAP_PRIVATE, 0, 0)

# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, 0, 0)
m = mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, 0, 0)
print m.find("\000")
m.close()

# Test mmap.mmap(0, 1, "shared", mmap.MAP_PRIVATE, 0, 0)
m = mmap.mmap(0, 1, "shared", mmap.MAP_PRIVATE, 0, 0)
print m.find("\000")
m.close()

