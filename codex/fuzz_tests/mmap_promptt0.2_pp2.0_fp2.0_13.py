import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/mmap_test', os.O_RDWR | os.O_CREAT)

# Set size
os.ftruncate(fd, 1024)

# Memory map file
m = mmap.mmap(fd, 1024, mmap.MAP_SHARED, mmap.PROT_WRITE)

# Write bytes
m.write(b'Hello Python!')

# Close map
m.close()

# Close file
os.close(fd)
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/mmap_test', os.O_RDWR | os.O_CREAT)

# Set size
os.ftruncate(fd, 1024)

# Memory map file
m = mmap.mmap(fd, 1024, mmap.MAP_SHARED, mmap.PROT_WRITE)

# Write bytes
m.write(b'Hello Python!')

# Close map
m.close()

# Close file
