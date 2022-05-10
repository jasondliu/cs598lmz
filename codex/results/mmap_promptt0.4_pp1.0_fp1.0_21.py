import mmap
# Test mmap.mmap()

# Open a file
fd = os.open('test.txt', os.O_RDWR)

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(fd, 0)

# Print the file
print m.readline()

# Close the map and file
m.close()
os.close(fd)

# Test mmap.mmap()

# Open a file
fd = os.open('test.txt', os.O_RDWR)

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(fd, 0)

# Read the content via standard file methods
print 'First 10 bytes via read :', m.read(10)

# Close the map and file
m.close()
os.close(fd)

# Test mmap.mmap()

# Open a file
fd = os.open('test.txt', os.O_RDWR)

# Create a memory-map to the file, size 0 means whole file
m = mmap.
