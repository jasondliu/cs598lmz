import mmap
# Test mmap.mmap()

# Open file
fd = os.open('../../data/test.txt', os.O_RDWR)

# Create mmap
m = mmap.mmap(fd, 0)

# Print content
print(m.readline())

# Close
