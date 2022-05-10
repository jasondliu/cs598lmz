import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print m.readline()

# Write to mmap
m.seek(0)
m.write('0123456789abcdef')

# Close mmap
m.close()

# Close file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print m.readline()

# Close mmap
m.close()

# Close file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print m.readline()

# Close mmap
m.close()

# Close file
f.close()

#
