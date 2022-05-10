import mmap
# Test mmap.mmap(0, 1, access=mmap.ACCESS_WRITE)
# Test mmap.mmap(-1, 1, access=mmap.ACCESS_WRITE)
# Test mmap.mmap(1, 0, access=mmap.ACCESS_WRITE)
# Test mmap.mmap(1, -1, access=mmap.ACCESS_WRITE)
# Test mmap.mmap(-1, -1, access=mmap.ACCESS_WRITE)
# Test mmap.mmap(1, 1, access=mmap.ACCESS_WRITE, offset=1)
# Test mmap.mmap(1, 1, access=mmap.ACCESS_WRITE, offset=-1)
# Test mmap.mmap(1, 1, access=mmap.ACCESS_WRITE, offset=1, tagname=1)
# Test mmap.mmap(1, 1, access=mmap.ACCESS_WRITE, offset=1, tagname=0)
# Test mmap.mmap(1, 1, access=mmap.ACC
