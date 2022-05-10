import mmap
# Test mmap.mmap(fd, length)
m = mmap.mmap(-1, 10)
print m.write("0123456789")
print m.seek(5)
print m.read(5)
m.close()
print

# Test mmap.mmap(fd, length, access=mmap.ACCESS_WRITE)
m = mmap.mmap(-1, 10, mmap.ACCESS_WRITE)
print m.write("0123456789")
print m.seek(5)
print m.read(5)
m.close()
print

# Test mmap.mmap(fd, length, access=mmap.ACCESS_READ)
m = mmap.mmap(-1, 10, mmap.ACCESS_READ)
print m.write("0123456789")
print m.seek(5)
print m.read(5)
m.close()
print

# Test mmap.mmap(fd, length, access=mmap.ACCESS_COPY)
m = mmap.mmap(-1, 10, mm
