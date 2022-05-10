import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using slice notation
# Note: new content must have same size
m[0:11] = b'Hello World'

# Close the map
m.close()

# Close the file
f.close()

# Open file
f = open('test.txt', 'r+')

# Read the modified content
print(f.readline())

# Close the file
f.close()

# Delete the file
os.remove('test.txt')

# Test mmap.mmap()

# Open file
f = open('test.txt', 'w+')

# Write some data
f.write('0123456789abcdef')

# Close the file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m =
