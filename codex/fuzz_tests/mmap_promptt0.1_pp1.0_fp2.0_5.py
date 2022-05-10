import mmap
# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')

# Write to the file
f.write('Hello World')

# Close the file
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory map
m = mmap.mmap(f.fileno(), 0)

# Read from the memory map
print(m.readline())

# Close the memory map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')

# Write to the file
f.write('Hello World')

# Close the file
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory map
m = mmap.mmap(f.fileno(), 0)

# Read from the memory map
print(m.readline())

# Close the memory map
m.close()

#
