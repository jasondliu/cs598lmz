import mmap
# Test mmap.mmap() to see whether it accepts the length parameter

print(mmap.mmap(-1, 10).size())

# Should have printed 10
print(mmap.mmap(-1, 10, length=10).size())

# Should have printed 10
print(mmap.mmap(-1, 10, length=10, offset=0).size())

# Should have printed 10
print(mmap.mmap(-1, 10, length=10, offset=0, access=mmap.ACCESS_READ).size())

# Should have printed 10
print(mmap.mmap(-1, 10, length=10, offset=0, access=mmap.ACCESS_WRITE).size())

# Should have printed 10
print(mmap.mmap(-1, 10, length=10, offset=0, access=mmap.ACCESS_COPY).size())

# Should have printed 10
print(mmap.mmap(-1, 10, length=10, offset=0, access=mmap.ACCESS_DEFAULT).size())

# Should have printed 10
print(
