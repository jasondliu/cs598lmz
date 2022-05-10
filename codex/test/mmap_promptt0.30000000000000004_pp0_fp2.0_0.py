import mmap
# Test mmap.mmap
import mmap

# Open file
f = open('test.txt', 'r+b')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

