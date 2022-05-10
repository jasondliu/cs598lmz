import mmap
# Test mmap.mmap

# Open the file
f = open('test.txt', 'r+')

# Create an mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
