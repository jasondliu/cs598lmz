import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# https://docs.python.org/2/library/mmap.html

# Open a file
f = open('/tmp/test.bin', 'r+b')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints "Hello Python!\n"

# Update content using slice notation;
# note that new content must have same size
m[6:11] = b'WORLD'

# ... and read again using standard file methods
m.seek(0)  # rewind
print(m.readline())  # prints "Hello WORLD!\n"

# close the map
m.close()

# close the file
f.close()
