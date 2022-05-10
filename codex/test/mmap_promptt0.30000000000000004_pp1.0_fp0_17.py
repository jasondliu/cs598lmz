import mmap
# Test mmap.mmap()

# Open file
fd = os.open("/tmp/test.txt", os.O_RDWR | os.O_CREAT)

# Create a memory map
m = mmap.mmap(fd, 0)

# Write to memory map
m.write("Hello world!")

# Close file descriptor
os.close(fd)

# Close memory map
m.close()
# Test mmap.mmap()

# Open file
fd = os.open("/tmp/test.txt", os.O_RDWR | os.O_CREAT)

# Create a memory map
m = mmap.mmap(fd, 0)
