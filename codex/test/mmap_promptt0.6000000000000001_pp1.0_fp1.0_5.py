import mmap
# Test mmap.mmap
import mmap
f = open('lorem.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
