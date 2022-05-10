import mmap
# Test mmap.mmap()
# https://docs.python.org/3/library/mmap.html

# Open a file
f = open('test.txt', 'r+')

# Create a memory-map to an existing file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print(m.readline())

# Write to the memory-map
m[0:11] = b'Hello world'

# Close the memory-map
m.close()

# Close the file
f.close()

# Open the file for reading
f = open('test.txt', 'r')

# Read the entire file
print(f.read())

# Close the file
f.close()

# Open the file for reading
f = open('test.txt', 'r')

# Create a memory-map to an existing file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print(m.readline())

# Close the memory-map
m.close()

#
