import mmap
# Test mmap.mmap()

# Create a file
with open('test.txt', 'w+') as f:
    f.write('Hello world!')

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using file methods
m.seek(0)
m.write(b'Hello Python!')

# Close the map
m.close()

# Close the file
f.close()

# Open the file
f = open('test.txt', 'r+')

# Read the entire file
print(f.readline())

# Close the file
f.close()

# Test mmap.mmap()

# Create a file
with open('test.txt', 'w+') as f:
    f.write('Hello world!')

# Open the file
f = open('test.txt', 'r+')

