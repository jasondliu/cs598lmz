import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints "Hello Python!\n"

# Update content using file methods
m.seek(0)  # rewind
m.write('O hello world!\n')

# Flush changes
m.flush()

# Close the map
m.close()

# Close the file
f.close()

# Open file
f = open('test.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints "O hello world!\n"

# Update content using file methods
m.seek(0)  # rewind
m.write('O hello world!\n')

# Flush changes
m.
