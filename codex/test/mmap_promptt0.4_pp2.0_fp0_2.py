import mmap
# Test mmap.mmap()

# Open file
fd = os.open(filename, os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

# Print entire file
print(m.read(100).decode('ascii'))

# Close file
os.close(fd)

# Close mmap object
m.close()

# Test mmap.mmap()

# Open file
fd = os.open(filename, os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

# Print entire file
print(m.read(100).decode('ascii'))

# Close file
os.close(fd)

# Close mmap object
m.close()

# Test mmap.mmap()

# Open file
