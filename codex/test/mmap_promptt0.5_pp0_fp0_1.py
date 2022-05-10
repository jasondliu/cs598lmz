import mmap
# Test mmap.mmap(0, size)
m = mmap.mmap(0, 100)
m[0] = 'a'
