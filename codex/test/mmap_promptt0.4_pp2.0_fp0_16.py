import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/test.dat', os.O_RDWR | os.O_CREAT)

# Write data
os.write(fd, '0123456789abcdef')

# Create mmap instance
m = mmap.mmap(fd, 16)

# Print entire buffer
