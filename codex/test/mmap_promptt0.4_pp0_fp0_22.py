import mmap
# Test mmap.mmap()

# Open the file for reading.
f = open('lorem.txt', 'r')

# Create a mmap object.
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Print the entire file.
print(m.readline())

# Close the map.
m.close()

# Close the file.
f.close()

# Test mmap.mmap()

# Open the file for writing.
f = open('lorem.txt', 'r+')

# Create a mmap object.
m = mmap.mmap(f.fileno(), 0)

# Write the string to the file.
m.write(b'0123456789abcdef')

# Close the map.
m.close()

# Close the file.
f.close()

# Open the file for reading.
f = open('lorem.txt', 'r')

# Create a mmap object.
