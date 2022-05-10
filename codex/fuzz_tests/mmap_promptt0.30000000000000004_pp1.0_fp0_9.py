import mmap
# Test mmap.mmap()

# Open file
fd = os.open('test.txt', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

# Print entire file
print m[:]

# Close file
os.close(fd)

# Test mmap.mmap()

# Open file
fd = os.open('test.txt', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

# Print entire file
print m[:]

# Close file
os.close(fd)

# Test mmap.mmap()

# Open file
fd = os.open('test.txt', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

# Print entire file
print m[:]

# Close file
os.close(fd)

# Test mmap.mmap()

# Open file
fd = os.open('test.txt', os.O_RDWR)

#
