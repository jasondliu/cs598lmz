import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

