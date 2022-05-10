import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.seek(0)

# Create memory-map
m = mmap.mmap(f.fileno(), 16)

# Read from file via memory-map
print m[4:8]

# Update memory-map
m[4:8] = 'AAAA'

# Flush changes
m.flush()

# Close file
f.close()

# Re-open file
f = open('/tmp/test.txt', 'r+')

# Read from file
print f.read(16)

# Close file
f.close()

# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.seek(0)

# Create memory-map
m = mmap.mmap(f.fileno(), 16)
