import mmap
# Test mmap.mmap(..., access=mmap.ACCESS_READ)
m = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)
print m.read(0)
print m.read(1)
print m.read(2)
print m.read(3)
print m.read(4)
print m.read(5)
print m.read(6)
print m.read(7)
print m.read(8)
m.close()

# Test mmap.mmap(..., access=mmap.ACCESS_WRITE)
m = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)
m.resize(8)
m.write('1234567')
m.close()

# Test mmap.mmap(..., access=mmap.ACCESS_COPY)
m = mmap.mmap(fd, 0, access=mmap.ACCESS_COPY)
# You can write to a copy-on-write map, but it doesn't do anything.
m.
