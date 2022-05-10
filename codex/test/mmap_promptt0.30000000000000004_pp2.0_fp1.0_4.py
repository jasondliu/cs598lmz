import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read content
print(m.read())

# Close mmap
m.close()

# Close file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Write content
m.write('Hello World')

# Close mmap
m.close()

# Close file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read content
print(m.read())

# Close mmap
m.close()

# Close file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create mmap
