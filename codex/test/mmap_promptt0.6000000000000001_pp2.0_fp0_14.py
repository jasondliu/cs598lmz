import mmap
# Test mmap.mmap()

# Open a file, ask for a memory-map of its contents
f = open("testfile", "r+")
m = mmap.mmap(f.fileno(), 0)

# Read the content via standard file methods
print(m.readline())
print(m.readline())
print(m.readline())

# Read the content via slice notation
print(m[:5])
print(m[6:15])

# Update content using slice notation;
# note that new content must have same size
m[6:15] = b"a short string"
print(m[6:15])

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap(fileno)

# Open a file, ask for a memory-map of its contents
f = open("testfile", "r+")

# Create a memory-map for the entire file
m = mmap.mmap(f.fileno(), 0)

