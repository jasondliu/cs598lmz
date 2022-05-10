import mmap
# Test mmap.mmap

# Open file
f = open("test.txt", "r+")

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using file methods
m.seek(0)
m.write(b"Hello Python!\n")

# Flush changes
m.flush()

# Close the map
m.close()

# Close the file
f.close()

# Open file
f = open("test.txt", "r+")

# Read the entire file
print(f.read())

# Close the file
f.close()

# Test mmap.mmap

# Open file
f = open("test.txt", "r+")

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using file methods
m.seek(0)
m.write(b"Hello Python!\n")
