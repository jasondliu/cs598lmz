import mmap
# Test mmap.mmap()

# Open file for memory-mapping
fd = os.open('lorem.txt', os.O_RDONLY)

# Create mmap instance
m = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)

# Read content via standard file methods
