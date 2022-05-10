import mmap
# Test mmap.mmap(-1, 12)

SIZE = 12
fd = os.open("hello.txt", os.O_CREAT|os.O_RDWR)

m = mmap.mmap(-1, SIZE, prot=mmap.ACCESS_READ)

# Must be a bug in CPython, because a native file descriptor is
# returned, but it's readonly.
#m = mmap.mmap(fd, SIZE)

print m.read(1)
#print m.write("hello world")
#print m.read(1)

print m.size()
print m.tell()

m.close()

# Test mmap.mmap(fd, 0)

m = mmap.mmap(fd, 0)

m.write("hello world")

print m.read(1)

m.close()

# Test mmap.mmap(fd, 0, mmap.ACCESS_READ)

m = mmap.mmap(fd, 0, mmap.ACCESS_READ)

print m.read(1)

