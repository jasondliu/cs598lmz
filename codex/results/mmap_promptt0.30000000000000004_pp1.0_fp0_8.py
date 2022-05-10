import mmap
# Test mmap.mmap()

# Open the file for reading
f = open('lorem.txt', 'r')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Print the first line of the file
print(m.readline())

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open the file for reading
f = open('lorem.txt', 'r')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read from the memory-map; this will return the whole file
print(len(m))
print(m[0:10])

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open the file for reading
f = open
