import mmap
# Test mmap.mmap()

# Read a file into memory
f = open("test.txt", 'r+b')
m = mmap.mmap(f.fileno(), 0)

# Print the entire file
