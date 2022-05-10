import mmap
# Test mmap.mmap()

# Create a file
f = open("test.txt", "w+")
f.write("Hello World")
f.close()

# Open the file
f = open("test.txt", "r+")

# Create a memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using slice notation
# Note: new content must have same size
m[6:] = " world!"

# See the modification
m.seek(0)
print(m.readline())

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Create a file
f = open("test.txt", "w+")
f.write("Hello World")
f.close()

# Open the file
f = open("test.txt", "r+")

# Create a memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
