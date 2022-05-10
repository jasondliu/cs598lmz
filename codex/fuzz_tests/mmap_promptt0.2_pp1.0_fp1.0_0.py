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

# Read from mmap
print m.readline()

# Close mmap
m.close()

# Close file
os.close(fd)

# Delete file
os.remove('/tmp/test.txt')

# Test mmap.mmap()

# Open file
fd = os.open('/tmp/test.txt', os.O_RDWR | os.O_CREAT)

# Write to file
os.write(fd, 'Hello world!')

# Close file
os.close(fd)

# Open file
fd = os.open('/tmp/test.txt
