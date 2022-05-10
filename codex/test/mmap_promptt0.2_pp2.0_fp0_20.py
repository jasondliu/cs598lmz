import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test.dat', 'r+b')

# Create mmap
m = mmap.mmap(f.fileno(), 0)
