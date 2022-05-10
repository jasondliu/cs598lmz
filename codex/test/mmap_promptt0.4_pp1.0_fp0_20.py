import mmap
# Test mmap.mmap()

# Create a file
f = open('/tmp/test.txt', 'w+')

# Write some data
f.write('Hello, world!')

# Close the file
f.close()

# Open the file
f = open('/tmp/test.txt', 'r+')

# Create a mmap
m = mmap.mmap(f.fileno(), 0)

# Read the file
print(m.readline())

# Close the mmap
m.close()

# Close the file
f.close()

# Remove the file
os.remove('/tmp/test.txt')

# Test mmap.mmap()

# Create a file
f = open('/tmp/test.txt', 'w+')

# Write some data
f.write('Hello, world!')

# Close the file
f.close()

# Open the file
f = open('/tmp/test.txt', 'r+')

# Create a mmap
m = mmap.mmap(f.fileno(), 0)

