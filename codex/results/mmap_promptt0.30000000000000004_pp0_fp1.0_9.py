import mmap
# Test mmap.mmap()

# Create a memory-mapped file
f = open('lorem.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Read the first line
print m.readline()

# Update the first line
m.seek(0)
m.write('Hello Python!')

# Read the modified file
m.seek(0)
print m.readline()

# Close the map
m.close()

# Close the underlying file
f.close()

# Test mmap.mmap()

# Create a memory-mapped file
f = open('lorem.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Read the first line
print m.readline()

# Update the first line
m.seek(0)
m.write('Hello Python!')

# Read the modified file
m.seek(0)
print m.readline()

# Close the map
m.close()

# Close the underlying file
f.close()


