import mmap
# Test mmap.mmap

# Open file
f = open('/tmp/test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.close()

# Open file
f = open('/tmp/test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read from file via memory map
print m[:]

# Update data in memory map
m[4:8] = 'abcd'

# Flush changes
m.flush()

# Close file
f.close()

# Open file
f = open('/tmp/test.txt', 'r+')

# Read from file
print f.read(16)

# Close file
f.close()

# Delete file
os.remove('/tmp/test.txt')

# Test mmap.mmap

# Open file
f = open('/tmp/test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')

