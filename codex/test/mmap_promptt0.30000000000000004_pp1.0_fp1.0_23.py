import mmap
# Test mmap.mmap

# Open a file
f = open('/tmp/test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
