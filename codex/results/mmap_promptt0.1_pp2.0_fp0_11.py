import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print file contents
print 'First 10 bytes via read :', m.read(10)

# Close the file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print file contents
print 'First 10 bytes via slice:', m[:10]

# Close the file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read from memory map
print 'First 10 bytes via read :', m.read(10)

# Reset file pointer
m.seek(0)

# Read from memory map
print 'First 10 bytes via read :', m.read(10)

# Close the file
f.close
