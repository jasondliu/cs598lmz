import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print m.readline()

# Close mmap
m.close()

# Close file
f.close()

# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print m.readline()

# Close mmap
m.close()

# Close file
f.close()

# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print m.readline()

# Close mmap
m.close()

# Close file
f
