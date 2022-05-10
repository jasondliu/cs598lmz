import mmap
# Test mmap.mmap

# Open file
f = open("test.txt", "r+")

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content
