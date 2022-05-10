import mmap
# Test mmap.mmap() for read-only access.
m = mmap.mmap(-1, 1024, access=mmap.ACCESS_READ)
# Test invalid file descriptor.
try:
    m = mmap.mmap(-2, 1024, access=mmap.ACCESS_READ)
except ValueError:
    print("ValueError")

# Test invalid length.
try:
    m = mmap.mmap(-1, -1, access=mmap.ACCESS_READ)
except ValueError:
    print("ValueError")

# Test invalid access
try:
    m = mmap.mmap(-1, 1024, access=mmap.ACCESS_WRITE)
except ValueError:
    print("ValueError")

# Test mmap.mmap() for write-only access.
m = mmap.mmap(-1, 1024, access=mmap.ACCESS_WRITE)
# Test mmap.mmap() for read/write access.
