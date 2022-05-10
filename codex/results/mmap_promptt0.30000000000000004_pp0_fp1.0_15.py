import mmap
# Test mmap.mmap

# Create a file
f = open('test.txt', 'w+')
f.write('Hello world!')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print m.readline()

# Update content using slice notation
# Note that new content must have same size
m[6:] = 'WORLD'

# See the modification
m.seek(0)
print m.readline()

# Close the map
m.close()

# Close the file
f.close()

# Open the file
f = open('test.txt', 'r+')

# Read the modified content
print f.readline()

# Close the file
f.close()

# Delete the file
os.remove('test.txt')

# Test mmap.mmap

# Create a file
f = open('test.txt', 'w+')
f.write('Hello
