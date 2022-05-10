import mmap
# Test mmap.mmap()

# Open a file
f = open("test.txt", "r+b")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints "Hello Python!\n"

# Update content using file methods
# ...

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open a file
f = open("test.txt", "r+b")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints "Hello Python!\n"

# Update content using file methods
m.seek(0)  # rewind
m.write(b"Hello World!\n")

# Close the map
m.close()

# Close the file
f
