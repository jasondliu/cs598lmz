import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, 0, 0)
# Test mmap.mmap(0, 1, "private", mmap.MAP_PRIVATE, 0, 0)
# Test mmap.mmap(0, 1, "copy-on-write", mmap.MAP_PRIVATE | mmap.MAP_COPY, 0, 0)
# Test mmap.mmap(0, 1, "copy-on-write", mmap.MAP_PRIVATE | mmap.MAP_COPY, 0, 0)
# Test mmap.mmap(-1, 1, "copy-on-write", mmap.MAP_PRIVATE | mmap.MAP_COPY, 0, 0)
# Test mmap.mmap(0, 1, "copy-on-write", mmap.MAP_PRIVATE | mmap.MAP_COPY, -1, 0)
# Test mmap.mmap(0, 1, "copy-on-write", mmap.MAP_PRIVATE | mmap.MAP_COP
