import mmap
# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')
f.write('Hello World!')
f.close()

# Open a file
f = open('test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print m.readline()

# Update content using file methods
m.seek(0)
m.write('Hello Python!')

# Close the map
m.close()

# See the change
f = open('test.txt', 'r+')
print f.readline()

# Close the file
f.close()

# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')
f.write('Hello World!')
f.close()

# Open a file
f = open('test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m
