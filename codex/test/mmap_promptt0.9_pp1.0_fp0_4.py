import mmap
# Test mmap.mmap() for a file descriptor
result = mmap.mmap(-1, os.fstat(fd).st_size, mmap.MAP_PRIVATE, mmap.PROT_WRITE, fd)
# Test mmap() for a path
result = mmap.mmap(fd, os.fstat(fd).st_size, mmap.MAP_SHARED, mmap.PROT_WRITE)
