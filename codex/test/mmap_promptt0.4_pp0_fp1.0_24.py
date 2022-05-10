import mmap
# Test mmap.mmap()

# Open a file for reading.
f = open('lorem.txt', 'r')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Print the entire file
print(m.readline())

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open a file for writing.
f = open('lorem.txt', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Print the entire file
print(m.readline())

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open a file for writing.
f = open('lorem.txt', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Print the entire file
