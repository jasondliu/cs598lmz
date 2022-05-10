import mmap
# Test mmap.mmap()

# Open file
fd = os.open('test.txt', os.O_RDWR)
# Memory-map the file, size 0 means whole file
m = mmap.mmap(fd, 0)
# Read content via standard file methods
print(m.readline())  # prints "Hello Python!\n"
# Update content using slice notation;
# note that new content must have same size
m[6:] = 'world'
# ... and read again using standard file methods
m.seek(0)
print(m.readline())  # prints "Hello world!\n"
# close the map
m.close()
# close the file
os.close(fd)

# Test mmap.mmap() with offset

# Open file
fd = os.open('test.txt', os.O_RDWR)
# Memory-map the file, size 0 means whole file, offset is where to start
m = mmap.mmap(fd, 13, 1)  # start at offset 13, 13 bytes long
# Read content via standard file methods
print(m.readline())
