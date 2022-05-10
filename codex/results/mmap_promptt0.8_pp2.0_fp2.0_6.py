import mmap
# Test mmap.mmap(-1, 100, mmap.MAP_PRIVATE)
with mmap.mmap(-1, 100, mmap.MAP_PRIVATE) as test_mmap:
    print test_mmap
    print repr(test_mmap)

# Test mmap.mmap(0, 100, mmap.MAP_PRIVATE)
with mmap.mmap(0, 100, mmap.MAP_PRIVATE) as test_mmap:
    print test_mmap
    print repr(test_mmap)

# Test mmap.mmap(1, 100, mmap.MAP_PRIVATE)
with mmap.mmap(1, 100, mmap.MAP_PRIVATE) as test_mmap:
    print test_mmap
    print repr(test_mmap)

# Test mmap.mmap(2, 100, mmap.MAP_PRIVATE)
with mmap.mmap(2, 100, mmap.MAP_PRIVATE) as test_mmap:
    print test_mmap
    print repr(test
