import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)
# Test mmap.mmap(0, 1, "private", mmap.MAP_PRIVATE)
# Test mmap.mmap(0, 1, "shared,private", mmap.MAP_SHARED|mmap.MAP_PRIVATE)
# Test mmap.mmap(0, 1, "private,shared", mmap.MAP_PRIVATE|mmap.MAP_SHARED)
# Test mmap.mmap(0, 1, "shared,private,shared", mmap.MAP_SHARED|mmap.MAP_PRIVATE|mmap.MAP_SHARED)
# Test mmap.mmap(0, 1, "private,shared,private", mmap.MAP_PRIVATE|mmap.MAP_SHARED|mmap.MAP_PRIVATE)
# Test mmap.mmap(0, 1, "shared,shared,private", mmap.MAP_SHARED|mmap.MAP_SHARED|mmap.MAP_PRIVATE)
