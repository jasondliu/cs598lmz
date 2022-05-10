import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read file
print(m.readline())

# Close file
m.close()
f.close()

# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read file
print(m.readline())

# Close file
m.close()
f.close()

# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read file
print(m.readline())

# Close file
m.close()
f.close()

# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

#
