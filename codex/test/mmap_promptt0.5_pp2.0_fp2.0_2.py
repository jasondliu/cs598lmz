import mmap
# Test mmap.mmap(0, 1, access=mmap.ACCESS_READ)
# Test mmap.mmap(-1, 1, access=mmap.ACCESS_READ)
# Test mmap.mmap(1, -1, access=mmap.ACCESS_READ)
# Test mmap.mmap(1, 1, access=mmap.ACCESS_READ)
# Test mmap.mmap(1, 1, access=mmap.ACCESS_WRITE)
# Test mmap.mmap(1, 1, access=mmap.ACCESS_COPY)
# Test mmap.mmap(1, 1, access=mmap.ACCESS_READ, tagname="")
# Test mmap.mmap(1, 1, access=mmap.ACCESS_READ, tagname=None)
# Test mmap.mmap(1, 1, access=mmap.ACCESS_READ, tagname="spam")
# Test mmap.mmap(1, 1, access=mmap.ACCESS_READ, tagname=1)
# Test mmap.mmap(
