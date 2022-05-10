import mmap
# Test mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE)
#
# This test is not meant to be run, just to be checked for errors.

# mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE)
mmap.mmap(0, 0)
mmap.mmap(0, 0, access=mmap.ACCESS_READ)
mmap.mmap(0, 0, access=mmap.ACCESS_COPY)
mmap.mmap(0, 0, access=mmap.ACCESS_WRITE)

# mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE, offset=0)
mmap.mmap(0, 0, offset=0)
mmap.mmap(0, 0, access=mmap.ACCESS_READ, offset=0)
mmap.mmap(0, 0, access=mmap.ACCESS_COPY, offset=0)
mmap.mmap(0, 0, access=mmap.ACCESS_WR
