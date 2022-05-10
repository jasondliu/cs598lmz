import mmap
# Test mmap.mmap() boundary condition.
mmap.mmap(256*1024*1024, 1)
