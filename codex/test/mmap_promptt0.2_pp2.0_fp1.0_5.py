import mmap
# Test mmap.mmap()

# Open file
f = open("test.txt", "r+b")

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Print file
