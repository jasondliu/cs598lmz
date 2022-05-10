import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using slice notation
# Note: new content must have same size
m[0:11] = 'Hello World'

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using slice notation
# Note: new content must have same size
m[0:11] = 'Hello World'

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()
