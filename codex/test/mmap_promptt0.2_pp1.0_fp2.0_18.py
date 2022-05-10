import mmap
# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')

# Write a string to the file
f.write('Hello, world!')

# Close the file
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-mapped file
