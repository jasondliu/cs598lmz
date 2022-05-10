import mmap
# Test mmap.mmap
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])

# Open file
fd = os.open("/tmp/testmmap", os.O_RDWR | os.O_CREAT)

# Set file size
os.ftruncate(fd, 4096)

# Create mapping
m = mmap.mmap(fd, 4096, access=mmap.ACCESS_WRITE)

# Write to file
m[:] = "Hello World"

# Close file
os.close(fd)

# Reopen the file
fd = os.open("/tmp/testmmap", os.O_RDONLY)

# Create mapping
m = mmap.mmap(fd, 4096, access=mmap.ACCESS_READ)

# Read from file
print m[:]

# Close file
os.close(fd)

# Cleanup
os.unlink("/tmp/testmmap")
