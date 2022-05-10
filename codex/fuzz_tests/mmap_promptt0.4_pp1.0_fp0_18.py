import mmap
# Test mmap.mmap

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Memory-map the file, size 0 means whole file
m = mmap.mmap(fd, 0)

# Read content via standard file methods
print("Before:", m.readline())  # b'This is the first line\n'

# Update content using slice notation;
# note that new content must have same size
m[6:] = b" world!\n"

# ... and read again using standard file methods
m.seek(0)
print("After: ", m.readline())  # b'Hello world!\n'

# close the map
m.close()

# close the file
os.close(fd)

# Memory-mapped files can also be used like any other file object, for example
# with the built-in open() function:

with open("foo.txt", "r+b") as f:
    # memory-map the file, size 0 means whole file
    m = mmap.mm
