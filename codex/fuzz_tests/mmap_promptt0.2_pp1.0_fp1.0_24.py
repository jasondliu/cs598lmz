import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints "Hello Python!"

# Update content using file's write method.
m.seek(0)
m.write('World')

# Flush changes
m.flush()

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints "Hello Python!"

# Update content using file's write method.
m.seek(0)
m.write('World')

# Flush changes
m.flush()

# Close the map
