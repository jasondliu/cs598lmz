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
print m.readline()

# Update the file
m.seek(0)
m.write('Hello, Python!')

# Close the memory-mapped file
m.close()

# Close the file
f.close()

# Open the file
f = open('test.txt', 'r+')

# Read from the file
print f.readline()

# Close the file
f.close()

# Delete the file
os.remove('test.txt')

# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')

# Write
