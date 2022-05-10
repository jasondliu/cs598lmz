import mmap
# Test mmap.mmap()

# Open a file for reading.
f = open('lorem.txt', 'r')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read from the mmap object
print(m.readline())

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open a file for reading.
f = open('lorem.txt', 'r')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read from the mmap object
print(m.readline())

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open a file for reading.
f = open('lorem.txt', 'r')

# Create a mmap object
m = mmap.mmap(f
