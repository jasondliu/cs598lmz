import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test.dat', 'r+b')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print m.readline()

# Write to mmap
m.write('0123456789abcdef')

# Seek
m.seek(0)

# Read from mmap
print m.readline()

# Close mmap
m.close()

# Close file
f.close()

# Test mmap.mmap()

# Open file
f = open('/tmp/test.dat', 'r+b')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print m.readline()

# Write to mmap
m.write('0123456789abcdef')

# Seek
m.seek(0)

# Read from mmap
print m.readline()

# Close mmap
m.close()

# Close file

