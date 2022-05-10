import mmap
# Test mmap.mmap(-1, 0)
# https://bugs.python.org/issue29053
with mmap.mmap(-1, 0) as m:
    pass

# Test mmap.mmap(-1, 0, mmap.MAP_PRIVATE)
# https://bugs.python.org/issue29053
with mmap.mmap(-1, 0, mmap.MAP_PRIVATE) as m:
    pass

# Test mmap.mmap(-1, 0, mmap.MAP_SHARED)
# https://bugs.python.org/issue29053
with mmap.mmap(-1, 0, mmap.MAP_SHARED) as m:
    pass

# Test mmap.mmap(-1, 0, mmap.MAP_SHARED, mmap.PROT_READ)
# https://bugs.python.org/issue29053
with mmap.mmap(-1, 0, mmap.MAP_SHARED, mmap.PROT_READ) as m:
    pass

# Test mmap.mmap(-
