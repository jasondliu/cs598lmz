import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/mmap_test', os.O_RDWR | os.O_CREAT)

# Set size
os.ftruncate(fd, 100)

# Map file
m = mmap.mmap(fd, 100)

# Write
m.write('Hello Python!')

# Read
print m.read(13)

# Close
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
m = mmap.mmap(fd, 100)

# Write
m.write('Hello Python!')

# Read
print m.read(13)

# Close
m.close()

# Close file
os.
