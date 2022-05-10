import mmap
# Test mmap.mmap()

# Create a file
with open('test.txt', 'w') as f:
    f.write('Hello, world!')

# Open the file
f = open('test.txt', 'r')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read from the memory-map
print m.readline()

# Close the memory-map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Create a file
with open('test.txt', 'w') as f:
    f.write('Hello, world!')

# Open the file
f = open('test.txt', 'r')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read from the memory-map
print m.readline()

# Close the memory-map
m.close()

#
