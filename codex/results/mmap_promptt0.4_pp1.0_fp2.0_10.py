import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Read content via slice notation
print(m[:5])

# Update content using slice notation;
# note that new content must have same size
m[6:] = ' world!\n'

# ... and read again using standard file methods
m.seek(0)
print(m.readline())

# close the map
m.close()

# close the file
f.close()

# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Read content via slice notation
print(m[:5])

# Update content using slice notation;
# note that new content must have same size
m
