import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print(m.readline())

# Update mmap
m.seek(0)
m.write(b'0123456789abcdef')
m.close()

# Close file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print(m.readline())

# Close mmap
m.close()

# Close file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print(m.readline())

# Close mmap
m.close()

# Close file
f.close()

