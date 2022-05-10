import mmap
# Test mmap.mmap(-1, 0)
m = mmap.mmap(-1, 0)
m.close()

# Test mmap.mmap(-1, 0, access=mmap.ACCESS_READ)
m = mmap.mmap(-1, 0, access=mmap.ACCESS_READ)
m.close()

# Test mmap.mmap(-1, 0, access=mmap.ACCESS_WRITE)
m = mmap.mmap(-1, 0, access=mmap.ACCESS_WRITE)
m.close()

# Test mmap.mmap(-1, 0, access=mmap.ACCESS_COPY)
m = mmap.mmap(-1, 0, access=mmap.ACCESS_COPY)
m.close()

# Test mmap.mmap(-1, 0, access=mmap.ACCESS_READ|mmap.ACCESS_WRITE)
m = mmap.mmap(-1, 0, access=mmap.ACCESS_READ|mmap.ACCESS_WRITE)
m.close()
