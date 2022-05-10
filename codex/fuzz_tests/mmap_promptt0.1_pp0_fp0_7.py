import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read content
print m.readline()

# Close file
f.close()

# Close mmap
m.close()

# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read content
print m.readline()

# Close file
f.close()

# Close mmap
m.close()

# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read content
print m.readline()

# Close file
f.close()

# Close mmap
m.close()

# Test mmap.mmap

# Open file
f = open
