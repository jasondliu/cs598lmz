import mmap
# Test mmap.mmap()

# Create file
f = open('/tmp/test.txt', 'wb')
f.write('Hello World')
f.close()

# Open file
