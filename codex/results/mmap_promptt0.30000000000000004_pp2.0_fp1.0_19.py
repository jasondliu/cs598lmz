import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read file
print 'First 10 bytes via read :', m.read(10)

# Reset file position
m.seek(0)

# Read file via slice
print 'First 10 bytes via slice:', m.read(10)

# Close mmap
m.close()

# Close file
f.close()

# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Write bytes
m.write('0123456789abcdef')

# Flush changes
m.flush()

# Close mmap
m.close()

# Close file
f.close()

# Open file
f = open('/tmp/test.txt', 'r+')

# Print file
print f.
