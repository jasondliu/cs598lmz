import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print(m.readline())

# Close file
f.close()

# Close mmap
m.close()

# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print(m.readline())

# Write to mmap
m.write(b'0123456789abcdef')

# Seek to beginning
m.seek(0)

# Read from mmap
print(m.readline())

# Close file
f.close()

# Close mmap
m.close()

# Test mmap.mmap()

