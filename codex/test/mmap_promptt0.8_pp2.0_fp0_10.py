import mmap
# Test mmap.mmap() does not segfault on zero-sized files.
with open("mmap_test", "wb") as fp:
    pass
