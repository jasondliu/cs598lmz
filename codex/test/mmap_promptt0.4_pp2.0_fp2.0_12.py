import mmap
# Test mmap.mmap()

# Open a file
f = open('test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

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
f.close()

# Test mmap.mmap()

# Open a file
f = open('test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
