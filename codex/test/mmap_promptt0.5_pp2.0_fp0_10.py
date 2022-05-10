import mmap
# Test mmap.mmap
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
