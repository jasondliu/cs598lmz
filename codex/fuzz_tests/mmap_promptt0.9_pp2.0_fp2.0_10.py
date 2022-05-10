import mmap
# Test mmap.mmap()
map = mmap.mmap(0, 4096, "..")
print map[:]
