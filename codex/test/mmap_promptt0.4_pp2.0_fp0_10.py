import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, fd, 0)
# Test mmap.mmap(0, 1, "private", mmap.MAP_PRIVATE, fd, 0)
# Test mmap.mmap(0, 1, "copy", mmap.MAP_COPY, fd, 0)
# Test mmap.mmap(0, 1, "private,copy", mmap.MAP_PRIVATE|mmap.MAP_COPY, fd, 0)

# Test mmap.mmap(0, 1, "shared,nonblock", mmap.MAP_SHARED|mmap.MAP_NONBLOCK, fd, 0)
# Test mmap.mmap(0, 1, "private,nonblock", mmap.MAP_PRIVATE|mmap.MAP_NONBLOCK, fd, 0)
# Test mmap.mmap(0, 1, "copy,nonblock", mmap.MAP_COPY|mmap.MAP_NONBLOCK, fd, 0)
#
