import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print file contents
print m.readline()

# Update content
m.seek(0)
m.write('0123456789abcdef')

# Close file
m.close()
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print file contents
print m.readline()

# Close file
m.close()
f.close()

# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print file contents
print m.readline()

# Update content
m.seek(0)
m.write('0123456789abcdef')

# Close file
