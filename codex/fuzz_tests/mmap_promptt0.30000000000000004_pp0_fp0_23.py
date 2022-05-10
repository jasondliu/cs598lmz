import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)
# Test mmap.mmap(0, 1, "private", mmap.MAP_PRIVATE)

# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, fileno=1)
# Test mmap.mmap(0, 1, "private", mmap.MAP_PRIVATE, fileno=1)

# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, fileno=1, offset=0)
# Test mmap.mmap(0, 1, "private", mmap.MAP_PRIVATE, fileno=1, offset=0)

# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, fileno=1, offset=0,
#                access=mmap.ACCESS_WRITE)
# Test mmap.mmap(0, 1, "private", mmap.MAP_PRIVATE, fileno=1, offset=0,
