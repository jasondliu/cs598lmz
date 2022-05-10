import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/mmap_test', os.O_RDWR | os.O_CREAT)

# Set size
os.ftruncate(fd, 100)

# Map file
m = mmap.mmap(fd, 0)

# Write to file
m.write('Hello Python!')

# Read from file
print m.read(11)

# Close map
m.close()

# Close file
os.close(fd)

# Delete file
os.remove('/tmp/mmap_test')

# Test mmap.mmap()

# Open file
fd = os.open('/tmp/mmap_test', os.O_RDWR | os.O_CREAT)

# Set size
os.ftruncate(fd, 100)

# Map file
m = mmap.mmap(fd, 0)

# Write to file
m.write('Hello Python!')

# Read from file
print m.read(11)

# Close map
m.
