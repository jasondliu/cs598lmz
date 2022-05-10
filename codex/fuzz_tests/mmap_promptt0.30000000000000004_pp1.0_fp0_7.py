import mmap
# Test mmap.mmap
# https://docs.python.org/3/library/mmap.html

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
# Note that new content must be the same size
# as the previous content
m[6:] = b"World"
m.seek(0)
print(m.readline())

# Close the map
m.close()

# Close the file
f.close()

# Open the file
f = open("test.txt", "r+")

# Read the entire file
print(f.readline())

# Close the file
f.close()

# Delete the file
os.remove("test.txt")

# Test mmap.mmap
# https://docs
