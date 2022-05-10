import mmap
# Test mmap.mmap()

# Create a string
str = '0123456789'

# Open a file
fd = os.open('data.txt', os.O_RDWR | os.O_CREAT)

# Write the string to the file
os.write(fd, str)

# Close the file descriptor
os.close(fd)

# Re-open the file
fd = os.open('data.txt', os.O_RDWR)

# Create a memory-map to the file
