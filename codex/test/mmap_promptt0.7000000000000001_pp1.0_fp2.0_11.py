import mmap
# Test mmap.mmap(-1, 12)

SIZE = 12
fd = os.open("hello.txt", os.O_CREAT|os.O_RDWR)

m = mmap.mmap(-1, SIZE, prot=mmap.ACCESS_READ)

# Must be a bug in CPython, because a native file descriptor is
# returned, but it's readonly.
#m = mmap.mmap(fd, SIZE)
