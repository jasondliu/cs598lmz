import mmap
# Test mmap.mmap()

# Create a file
f = open("foo", "wb")
f.write("Hello world")
f.close()

# Open the file for reading
f = open("foo", "r+")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
