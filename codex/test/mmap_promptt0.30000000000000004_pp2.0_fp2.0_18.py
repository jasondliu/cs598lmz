import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/mmap_test', os.O_RDWR | os.O_CREAT)

# Set size
os.ftruncate(fd, 1024)

# Map file
m = mmap.mmap(fd, 1024, mmap.MAP_SHARED, mmap.PROT_WRITE)

# Write to file
m.write('Hello World')

# Close file
m.close()
os.close(fd)
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/mmap_test', os.O_RDWR | os.O_CREAT)

# Set size
os.ftruncate(fd, 1024)

# Map file
m = mmap.mmap(fd, 1024, mmap.MAP_SHARED, mmap.PROT_WRITE)

# Write to file
m.write('Hello World')

# Close file
m.close()
os.close(fd)
# Test mmap.mmap()
