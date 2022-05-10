import mmap
# Test mmap.mmap(0, size, prot, flags)
size = mmap.PAGESIZE
m = mmap.mmap(0, size, mmap.ACCESS_READ, mmap.MAP_SHARED, 0)
# Test mmap.mmap(0, size, prot, flags, fd)
m = mmap.mmap(0, size, mmap.ACCESS_READ, mmap.MAP_SHARED, 0)
# Test mmap.mmap(0, size, prot, flags, fd, 0)
m = mmap.mmap(0, size, mmap.ACCESS_READ, mmap.MAP_SHARED, 0, 0)
# Test mmap.mmap(0, size, prot, flags, fd, offset)
m = mmap.mmap(0, size, mmap.ACCESS_READ, mmap.MAP_SHARED, 0, 0)
# Test mmap.mmap(0, size, prot, flags, fd, offset)
m = mmap.mmap(0, size, mmap.ACCESS_
