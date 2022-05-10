import mmap
# Test mmap.mmap()

# Open file
f = open('test.dat', 'rb')

# Create memory-map
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read whole file
print(m.readline())

# Close the file
f.close()

# Close the memory-map
m.close()

# Test mmap.mmap()

# Open file
f = open('test.dat', 'rb')

# Create memory-map
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read whole file
print(m.readline())

# Close the file
f.close()

# Close the memory-map
m.close()

# Test mmap.mmap()

# Open file
f = open('test.dat', 'rb')

# Create memory-map
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read whole file
print
