import mmap
# Test mmap.mmap()

# Open file for memory-mapping
fd = os.open('lorem.txt', os.O_RDONLY)

# Create mmap instance
m = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)

# Read content via standard file methods
print 'First 10 bytes via read :', m.read(10)

# Read content via slice notation
print 'First 10 bytes via slice:', m[:10]

# Read content via buffer slice notation
print 'First 10 bytes via buffer:', m[0:10]

# Close the mmap instance
m.close()

# Close the original file
os.close(fd)

# Open file for memory-mapping
fd = os.open('lorem.txt', os.O_RDWR)

# Create mmap instance
m = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)

# Print the original file
print 'Before update:', m[:]

# Update a portion of the memory-mapped file
m[0
