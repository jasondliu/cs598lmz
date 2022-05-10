import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline().rstrip())

# Update content using slice notation
# Note that new content must have same size
m[6:] = ' world!\n'

# Flush changes
m.flush()

# Close the map
m.close()

# Close the file
f.close()

# Open file to see the changes
f = open('test.txt', 'r+')
print(f.readline().rstrip())
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline().rstrip())

# Update content using slice notation
# Note that new content must have same size
m[6:] = ' world!\n'

#
