import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using file's write method
m.seek(0)
m.write(b'0123456789abcdef')

# Close the map
m.close()

# Close the file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Close the map
m.close()

# Close the file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Close the map
m
