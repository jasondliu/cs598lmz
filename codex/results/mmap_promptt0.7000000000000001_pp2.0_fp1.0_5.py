import mmap
# Test mmap.mmap.__new__():
#   The class can be instantiated.

# Read-only.
m = mmap.mmap(-1, 1024, access=mmap.ACCESS_READ)
m.close()

# Read-write.
m = mmap.mmap(-1, 1024, access=mmap.ACCESS_WRITE)
m.close()

# Copy-on-write.
m = mmap.mmap(-1, 1024, access=mmap.ACCESS_COPY)
m.close()

# Default.
m = mmap.mmap(-1, 1024)
m.close()
