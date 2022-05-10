import mmap
# Test mmap.mmap.read()

# Create a file
with open('test.txt', 'w') as f:
    f.write('Hello world!')

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.read(11))

# Read content via slice notation
print(m[:11])

# Update content using slice notation;
# note that new content must have same size
m[6:] = b'world'

# ... and read again using standard file methods
m.seek(0)
print(m.read(11))

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap.write()

# Create a file
with open('test.txt', 'w') as f:
    f.write('Hello world!')

# Open the file
f = open('test.txt', '
