import mmap
# Test mmap.mmap()
m = mmap.mmap(0, 1, "test")
m.write("a")
m.seek(0)
print m.read()
m.close()

# Test mmap.mmap(fd, size)
m = mmap.mmap(-1, 1)
m.write("a")
m.seek(0)
print m.read()
m.close()

# Test mmap.mmap(fd, size, access)
m = mmap.mmap(-1, 1, mmap.ACCESS_READ)
m.write("a")
m.seek(0)
print m.read()
m.close()

# Test mmap.mmap(fd, size, access, flags)
m = mmap.mmap(-1, 1, mmap.ACCESS_READ, mmap.MAP_PRIVATE)
m.write("a")
m.seek(0)
print m.read()
m.close()

# Test mmap.mmap(fd, size, access, flags, prot)
m = mmap.
