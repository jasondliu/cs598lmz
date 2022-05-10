import mmap
# Test mmap.mmap()

# Open file for reading
fd = os.open('lorem.txt', os.O_RDONLY)

# Create new mmap object
m = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)

# Read from mmap'ed file
print('First 10 bytes via read :', m.read(10))

# Close the open file
os.close(fd)

# Open file for writing
fd = os.open('lorem.txt', os.O_RDWR)

# Create mmap object, size 0 means whole file
m = mmap.mmap(fd, 0)

# Write to mmap'ed file
m.write(b'0123456789abcdef')

# Close the open file
os.close(fd)

# Open file for reading
fd = os.open('lorem.txt', os.O_RDONLY)

# Create mmap object, size 0 means whole file
m = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)


