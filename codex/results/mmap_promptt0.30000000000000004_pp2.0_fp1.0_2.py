import mmap
# Test mmap.mmap.read_byte()

# Create a file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

# Open the file
f = open("hello.txt", "r+b")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Print the content via the memory-mapped file
print(m.readline())

# Update content using slice notation;
# note that new content must have same size
m[6:12] = b"world"

# See the modification
m.seek(0)
print(m.readline())

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap.move()

# Create a file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

# Open the file
f = open("hello.txt", "r+b")


