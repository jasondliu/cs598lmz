import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/test.txt', os.O_RDWR | os.O_CREAT)

# Write to file
os.write(fd, 'Hello world!')

# Close file
os.close(fd)

# Open file
fd = os.open('/tmp/test.txt', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

