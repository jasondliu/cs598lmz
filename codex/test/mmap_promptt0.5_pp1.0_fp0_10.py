import mmap
# Test mmap.mmap()

# Create file
with open("test.txt", "wb") as f:
    f.write("Test data\n")

# Open file
with open("test.txt", "rb") as f:
    # Create memory-mapped file
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # Read file
