import mmap
# Test mmap.mmap(fileno, length)
m = mmap.mmap(-1, 1)
m.close()

# Test mmap.mmap(fileno, length, access=ACCESS_READ)
m = mmap.mmap(-1, 1, mmap.ACCESS_READ)
m.close()

# Test mmap.mmap(fileno, length, access=ACCESS_WRITE)
m = mmap.mmap(-1, 1, mmap.ACCESS_WRITE)
m.close()

# Test mmap.mmap(fileno, length, access=ACCESS_COPY)
m = mmap.mmap(-1, 1, mmap.ACCESS_COPY)
m.close()

# Test mmap.mmap(fileno, length, flags=MAP_SHARED)
m = mmap.mmap(-1, 1, flags=mmap.MAP_SHARED)
m.close()

# Test mmap.mmap(fileno, length, flags=MAP_PRIVATE)
