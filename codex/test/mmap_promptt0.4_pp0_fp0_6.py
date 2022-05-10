import mmap
# Test mmap.mmap()

# Open file for reading and writing
f = open('test.txt', 'r+')

# Create mmap starting at page boundary
m = mmap.mmap(f.fileno(), 0)

