import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'r+b')

# Memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
