import mmap
# Test mmap.mmap()

# Open a file
fd = os.open("foo.txt", os.O_RDWR)

# Memory-map the file, size 0 means whole file
m = mmap.mmap(fd, 0)

# Read content via standard file methods
print m.readline()

# Update content using slice notation;
# note that new content must have same size
m[0:11] = "Hello, world"

# ... and read again using standard file methods
m.seek(0)
print m.readline()

# close the map
m.close()

# close the file
os.close(fd)

# Test mmap.mmap()

# Open a file
fd = os.open("foo.txt", os.O_RDWR)

# Memory-map the file, size 0 means whole file
m = mmap.mmap(fd, 0)

# Read content via standard file methods
print m.readline()

# Update content using slice notation;
# note that new content must have same size
m[0:11] = "Hello
