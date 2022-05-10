import mmap
# Test mmap.mmap(0, 0)
m = mmap.mmap(0, 0)
# Test mmap.mmap(0, 0, access=mmap.ACCESS_READ)
m = mmap.mmap(0, 0, access=mmap.ACCESS_READ)
# Test mmap.mmap(0, 0, access=mmap.ACCESS_WRITE)
m = mmap.mmap(0, 0, access=mmap.ACCESS_WRITE)
