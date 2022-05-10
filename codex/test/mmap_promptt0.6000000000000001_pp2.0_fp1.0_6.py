import mmap
# Test mmap.mmap() and mmap.ACCESS_* constants
print(mmap.mmap(-1, 1))
print(mmap.ACCESS_READ)
print(mmap.ACCESS_WRITE)
print(mmap.ACCESS_COPY)
print(mmap.MAP_SHARED)
print(mmap.MAP_PRIVATE)
print(mmap.MAP_ANONYMOUS)
print(mmap.MAP_ANON)
# Test mmap.error exception
try:
    m = mmap.mmap(-1, 1)
    m.write_byte(b'a')
except mmap.error as e:
    print(e)
# Test mmap.mmap() with invalid arguments
try:
    m = mmap.mmap(-1, 1, access=mmap.ACCESS_READ)
except ValueError as e:
    print(e)
try:
    m = mmap.mmap(-1, 1, access=mmap.ACCESS_WRITE)
except ValueError as e:
    print(e)
