import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/test.txt', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

# Read from mmap
print(m.readline())

# Close file
os.close(fd)

# Test mmap.mmap() with length

# Open file
fd = os.open('/tmp/test.txt', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, mmap.PAGESIZE)

# Read from mmap
print(m.readline())

# Close file
os.close(fd)

# Test mmap.mmap() with offset

# Open file
fd = os.open('/tmp/test.txt', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, mmap.PAGESIZE, offset=mmap.PAGESIZE)

# Read from mmap
print(m.readline())

# Close
