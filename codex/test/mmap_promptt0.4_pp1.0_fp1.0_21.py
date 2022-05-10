import mmap
# Test mmap.mmap()

# Open a file
fd = os.open('test.txt', os.O_RDWR)

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(fd, 0)

# Print the file
