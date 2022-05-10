import mmap
# Test mmap.mmap()

# Create a file and open it
with open("test.txt", "wb") as f:
    f.write(b"Hello Python!\n")

# Open the file
f = open("test.txt", "r+b")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using slice assignment
# Note that new content must have same size
m[6:] = b" world!\n"
m.flush()

# Close the map and file
m.close()
f.close()

# Open the file again and read the modification
f = open("test.txt", "rb")
print(f.readline())

# Clean up
f.close()
os.remove("test.txt")

# Test mmap.mmap()

# Create a file and open it
with open("test.txt", "wb") as f:
    f.write(b"Hello Python
