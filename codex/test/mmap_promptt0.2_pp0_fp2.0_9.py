import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+b')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
