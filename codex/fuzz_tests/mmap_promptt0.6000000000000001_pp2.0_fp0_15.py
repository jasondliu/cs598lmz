import mmap
# Test mmap.mmap().
m = mmap.mmap(0, 1, "a", mmap.MAP_PRIVATE, -1, 0)
m.close()

# Test mmap.mmap().
m = mmap.mmap(0, 1, "a", mmap.MAP_PRIVATE, -1, 0)
m.resize(10)
m.close()

# Test mmap.mmap().
m = mmap.mmap(0, 1, "a", mmap.MAP_PRIVATE, -1, 0)
m.resize(0)
m.close()

# Test mmap.mmap().
m = mmap.mmap(0, 1, "a", mmap.MAP_PRIVATE, -1, 0)
m.resize(0)
m.close()

# Test mmap.mmap().
m = mmap.mmap(0, 1, "a", mmap.MAP_PRIVATE, -1, 0)
m.resize(10)
m.close()

# Test mmap.
