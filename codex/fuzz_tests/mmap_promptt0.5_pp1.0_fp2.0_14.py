import mmap
# Test mmap.mmap(0, 0)
m = mmap.mmap(0, 0)
# Test mmap.mmap(0, 0, access=mmap.ACCESS_READ)
m = mmap.mmap(0, 0, access=mmap.ACCESS_READ)
# Test mmap.mmap(0, 0, access=mmap.ACCESS_WRITE)
m = mmap.mmap(0, 0, access=mmap.ACCESS_WRITE)
# Test mmap.mmap(0, 0, access=mmap.ACCESS_COPY)
m = mmap.mmap(0, 0, access=mmap.ACCESS_COPY)
# Test mmap.mmap(0, 0, access=mmap.ACCESS_DEFAULT)
m = mmap.mmap(0, 0, access=mmap.ACCESS_DEFAULT)
# Test mmap.mmap(0, 0, access=mmap.ACCESS_DEFAULT, offset=0)
m = mmap.mmap(0, 0, access=mmap
