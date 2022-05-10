import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print repr(m.readline())

# Update content using slice notation;
# note that new content must have same size
m[0:11] = 'Hello World'

# ... and read again using standard file methods
m.seek(0)
print repr(m.readline())

# close the map
m.close()

# close the file
f.close()

# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print repr(m.readline())

# Update content using slice notation;
# note that new content must have same size
m[0:11]
