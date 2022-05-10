import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print 'First 10 bytes via read :', m.read(10)

# Reset file position
m.seek(0)

# Read content via slice notation
print 'First 10 bytes via slice:', m.read(10)

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print 'First 10 bytes via read :', m.read(10)

# Reset file position
m.seek(0)

# Read content via slice notation
print 'First 10 bytes via slice:', m.read(10)

# Close the map
m.close()

# Close the
