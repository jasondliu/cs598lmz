import mmap
# Test mmap.mmap()

# Create a file to read and write
f = open('/tmp/mmap_test', 'w+')

# Write a few bytes
f.write('0123456789abcdef')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 16, access=mmap.ACCESS_WRITE)

# Read the content via standard file methods
print 'f.read(10):', f.read(10)

# Update content using slice notation;
# note that new content must have same size
m[4:8] = 'AAAA'

# See what happened
print 'f.read(16):', f.read(16)

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Create a file to read and write
f = open('/tmp/mmap_test', 'w+')

# Write a few bytes
f.write('0123456789abcdef')

# Create a memory-map to the file

