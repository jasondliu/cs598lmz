import mmap
# Test mmap.mmap()

# Create a file to read and write
f = open('/tmp/mmap_test', 'w+')

# Write a few bytes
f.write('0123456789abcdef')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 16, access=mmap.ACCESS_WRITE)

# Read the content via standard file methods
