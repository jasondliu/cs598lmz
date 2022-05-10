import mmap
# Test mmap.mmap()

# Create a file
f = open('/tmp/test.txt', 'w+')
f.write('Hello World')
f.close()

# Open the file
f = open('/tmp/test.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
