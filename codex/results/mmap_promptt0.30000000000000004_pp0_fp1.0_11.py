import mmap
# Test mmap.mmap

# Open a file for writing
f = open('test.txt', 'w+')

# Write a string to the file
f.write('Hello World!')

# Close the file
f.close()

# Open the file for reading
f = open('test.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print m[:]

# Close the memory-map
m.close()

# Close the file
f.close()

# Open a file for writing
f = open('test.txt', 'w+')

# Write a string to the file
f.write('Hello World!')

# Close the file
f.close()

# Open the file for reading
f = open('test.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print m[:]

# Close the memory-
