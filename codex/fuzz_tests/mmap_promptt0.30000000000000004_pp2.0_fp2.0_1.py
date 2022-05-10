import mmap
# Test mmap.mmap()

# Open file for reading
f = open('lorem.txt', 'r')

# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Print entire file
print 'First 10 bytes via read :', m.read(10)
print 'First 10 bytes via slice:', m[:10]
print '2nd   10 bytes via read :', m.read(10)

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file for reading
f = open('lorem.txt', 'r')

# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read from position 10
m.seek(10)
print 'Characters after 10 :', m.read(10)

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

