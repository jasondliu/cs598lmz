import mmap
# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')
f.write('Hello World!')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print(m.readline())

# Update the memory-map with new data
m.seek(0)
m.write('Hello World!')

# Close the memory-map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')
f.write('Hello World!')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print(m.readline())

