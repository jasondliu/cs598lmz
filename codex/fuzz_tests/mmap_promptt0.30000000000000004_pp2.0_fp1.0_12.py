import mmap
# Test mmap.mmap()

# Open a file
fd = os.open('/tmp/test.txt', os.O_RDWR | os.O_CREAT)

# Create a memory-map to the file.  Size 0 means
# whole file, starting at offset 0.
m = mmap.mmap(fd, 0)

# Print the file
print m.readline()

# Close the map and the file
m.close()
os.close(fd)

# Test mmap.mmap()

# Open a file
fd = os.open('/tmp/test.txt', os.O_RDWR | os.O_CREAT)

# Create a memory-map to the file.  Size 0 means
# whole file, starting at offset 0.
m = mmap.mmap(fd, 0)

# Print the file
print m.readline()

# Close the map and the file
m.close()
os.close(fd)

# Test mmap.mmap()

# Open a file
fd = os.open('/tmp/test.txt',
