import mmap
# Test mmap.mmap.read()

# Open a file for reading
f = open('/tmp/test.txt', 'r')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read content via standard file methods
print(m.readline())
print(m.readline())

# Read content via slice notation
print(m[:5])

# Update content using slice notation;
# note that new content must have same size
# m[6:11] = b'world'

# ... and read again using standard file methods
# m.seek(0)
# print(m.readline())

# close the map
m.close()

# close the file
f.close()
