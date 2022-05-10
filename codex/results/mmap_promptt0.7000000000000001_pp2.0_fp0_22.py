import mmap
# Test mmap.mmap()
m = mmap.mmap(-1, 1024)
m.write("Hello")
m.read(1024)

# mmap.ACCESS_COPY
m = mmap.mmap(-1, 1024, access=mmap.ACCESS_COPY)
m.write("Hello")
m.read(1024)

# mmap.ACCESS_READ
try:
    m = mmap.mmap(-1, 1024, access=mmap.ACCESS_READ)
    m.write("Hello")
except ValueError, msg:
    pass

# mmap.ACCESS_WRITE
try:
    m = mmap.mmap(-1, 1024, access=mmap.ACCESS_WRITE)
    m.read(1024)
except ValueError, msg:
    pass

# mmap.MAP_SHARED
m = mmap.mmap(-1, 1024, mmap.MAP_SHARED)
m.write("Hello")
m.read(1024)

# mmap.MAP_PRIVATE
try:
    m
