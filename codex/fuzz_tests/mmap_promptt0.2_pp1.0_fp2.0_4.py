import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using file methods
m.seek(0)
m.write(b'0123456789abcdef')

# Read from position 5
m.seek(5)
print(m.read(1))

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using file methods
m.seek(0)
m.write(b'0123456789abcdef')

# Read from position 5
m.seek(5)
print(m.read(1))


