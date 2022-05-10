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
