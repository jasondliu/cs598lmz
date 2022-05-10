import mmap
# Test mmap.mmap()

# Open a file
fd = os.open('/tmp/test.txt', os.O_RDWR | os.O_CREAT)

# Write a string to the file
os.write(fd, b'Hello World!')

# Close the file descriptor
os.close(fd)

# Open the file for reading
fd = os.open('/tmp/test.txt', os.O_RDONLY)

# Create a memory map
m = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)

# Read from the memory map
print(m.read(11))

# Close the file descriptor
os.close(fd)

# Close the memory map
m.close()

# Delete the file
os.remove('/tmp/test.txt')
