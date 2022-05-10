import mmap
# Test mmap.mmap()

# Open file and get size
f = open("test.txt", "r+")
f.write("1234567890" * 100)
f.seek(0)

# Map file
m = mmap.mmap(f.fileno(), 0)

# Read from file
