import mmap
# Test mmap.mmap()

# Open file
f = open('data.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints "Hello Python!\n"

# Update content using file methods
m.seek(0)  # rewind
m.write('Hello World!\n')

# Flush changes
m.flush()

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file
f = open('data.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints "Hello World!\n"

# Update content using file methods
m.seek(0)  # rewind
