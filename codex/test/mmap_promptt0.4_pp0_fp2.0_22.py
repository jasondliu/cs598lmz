import mmap
# Test mmap.mmap(0,1)
with mmap.mmap(0, 1) as m:
    pass

# Test mmap.mmap(-1,1)
with mmap.mmap(-1, 1) as m:
    pass

# Test mmap.mmap(0,1,mmap.MAP_SHARED)
with mmap.mmap(0, 1, mmap.MAP_SHARED) as m:
    pass

# Test mmap.mmap(-1,1,mmap.MAP_SHARED)
with mmap.mmap(-1, 1, mmap.MAP_SHARED) as m:
    pass

# Test mmap.mmap(0,1,mmap.MAP_PRIVATE)
with mmap.mmap(0, 1, mmap.MAP_PRIVATE) as m:
    pass

# Test mmap.mmap(-1,1,mmap.MAP_PRIVATE)
with mmap.mmap(-1, 1, mmap.MAP_PRIVATE) as m:
    pass
