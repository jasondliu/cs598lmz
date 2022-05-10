import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print file contents
print 'First 10 bytes via read :', m.read(10)

# Close map and file
m.close()
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read from position 0
m.seek(0)

# Write 2 bytes
m.write('ab')

# Read from position 0
m.seek(0)

# Print file contents
print 'First 10 bytes via read :', m.read(10)

# Close map and file
m.close()
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read from position 0
m.seek(0)

