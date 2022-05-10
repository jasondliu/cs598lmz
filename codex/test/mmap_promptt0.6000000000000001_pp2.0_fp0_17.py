import mmap
# Test mmap.mmap(fd, length, access=mmap.ACCESS_WRITE)
# Bug was segfaulting.

f = open('/dev/null', 'wb')
m = mmap.mmap(f.fileno(), 0, mmap.ACCESS_WRITE)
f.close()
