import mmap
# Test mmap.mmap for read-only access
m = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
