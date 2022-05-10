import mmap
# Test mmap.mmap()

# Open file for reading
fd = os.open('lorem.txt', os.O_RDONLY)

# Create mmap object
m = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)

# Read some data
print('First 10 bytes via read :', m.read(10))

# Close the file
os.close(fd)

# Open file for writing
fd = os.open('lorem.txt', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

# Write some data
m.write(b'0123456789abcdef')

# Close the file
os.close(fd)

# Open file for reading
fd = os.open('lorem.txt', os.O_RDONLY)

# Create mmap object
m = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)

# Read some data
print('First 10 bytes via read :', m.read(10))

#
