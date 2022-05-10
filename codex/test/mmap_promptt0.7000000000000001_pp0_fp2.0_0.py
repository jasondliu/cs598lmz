import mmap
# Test mmap.mmap()
f = open('lorem.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
