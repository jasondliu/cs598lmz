import mmap
# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 16)

# Read content via standard file methods
print 'f.read(10):', f.read(10)

# Read content via mmap memory
print 'm.read(10):', m.read(10)

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 16)

# Read content via
