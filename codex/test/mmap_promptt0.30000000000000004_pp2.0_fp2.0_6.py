import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
