import mmap
# Test mmap.mmap()

# Open file for reading
f = open('lorem.txt', 'r')

# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read first 10 bytes
print(m.read(10))

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file for reading
f = open('lorem.txt', 'r')

# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read some data
print(m[:10])

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file for reading
f = open('lorem.txt', 'r')

# Create mmap object
