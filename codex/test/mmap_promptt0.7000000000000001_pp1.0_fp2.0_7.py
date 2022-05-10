import mmap
# Test mmap.mmap(0, 1, "", mmap.ACCESS_READ) with a small size and ACCESS_READ.
# This used to cause a crash on Linux.
