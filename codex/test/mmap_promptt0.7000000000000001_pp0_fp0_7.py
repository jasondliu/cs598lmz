import mmap
# Test mmap.mmap()

size = 1024

with open('./test.txt', 'r+') as f:
    mm = mmap.mmap(f.fileno(), size)
