import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read from file via memory map
print m[:]

# Update file from memory map
# Note that new content must be same size or smaller
m[6:] = 'Hello World'

# Close file
m.close()
f.close()

# Open file
f = open('test.txt', 'r+')

# Print file contents
print f.readline()

# Close file
f.close()

# Delete file
os.remove('test.txt')

# Test mmap.mmap()

# Open file
f = open('test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.close()

# Open file

