import mmap
# Test mmap.mmap(fd, length, flags, prot, access, offset)
m = mmap.mmap(-1, 4096)
m[0:10] = "0123456789"
