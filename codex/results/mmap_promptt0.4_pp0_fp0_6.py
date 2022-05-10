import mmap
# Test mmap.mmap()

# Open file for reading and writing
f = open('test.txt', 'r+')

# Create mmap starting at page boundary
m = mmap.mmap(f.fileno(), 0)

# Print length and content of file
print 'Before:\n', m.readline(),

# Re-position at the beginning of the mmap
m.seek(0)

# Write to file
m.write('0123456789abcdef')

# Re-position at the beginning of the mmap
m.seek(0)

# Print length and content of file
print 'After:\n', m.readline()

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file for reading and writing
f = open('test.txt', 'r+')

# Create mmap starting at page boundary
m = mmap.mmap(f.fileno(), 0)

# Print length and content of file
print 'Before:\n', m.readline(),

# Re
