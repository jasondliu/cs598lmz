import mmap
# Test mmap.mmap(0, 1)
m = mmap.mmap(0, 1)
m.write('\0')
