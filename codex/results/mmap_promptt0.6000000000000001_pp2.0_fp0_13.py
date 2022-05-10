import mmap
# Test mmap.mmap(0, 1, access=mmap.ACCESS_WRITE)
# See issue #27260
print('Test 1')
with mmap.mmap(0, 1, access=mmap.ACCESS_WRITE) as m:
    pass

# Test mmap.mmap(-1, 1, access=mmap.ACCESS_WRITE)
print('Test 2')
with mmap.mmap(-1, 1, access=mmap.ACCESS_WRITE) as m:
    pass

# Test mmap.mmap(0, 1, access=mmap.ACCESS_READ)
print('Test 3')
with mmap.mmap(0, 1, access=mmap.ACCESS_READ) as m:
    pass

# Test mmap.mmap(-1, 1, access=mmap.ACCESS_READ)
print('Test 4')
with mmap.mmap(-1, 1, access=mmap.ACCESS_READ) as m:
    pass
