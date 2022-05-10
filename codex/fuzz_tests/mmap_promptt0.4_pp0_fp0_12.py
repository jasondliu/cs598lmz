import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/mmap_test_file', 'w+')

# Write some data to file
f.write('Hello Python!')
f.seek(0)

# Create memory-map to file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using slice notation;
# note that new content must have same size
m[6:] = ' world'
m.seek(0)
print(m.readline())

# Close the map and file
m.close()
f.close()

# Test memory-mapped file

# Open file
f = open('/tmp/mmap_test_file', 'r+')

# Create memory-map to file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using slice notation;
# note that new content must have same size
m[6:] = 'Python!'
