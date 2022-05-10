import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/test.txt', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

# Print mmap object
print(m)

# Close file
os.close(fd)

# Close mmap object
m.close()

# Open file
fd = os.open('/tmp/test.txt', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

# Read mmap object
print(m.read())

# Close file
os.close(fd)

# Close mmap object
m.close()

# Open file
fd = os.open('/tmp/test.txt', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

# Write to mmap object
m.write(b'Hello')

# Close file
os.close(fd)

# Close mmap object
m.close()
