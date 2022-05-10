import mmap
# Test mmap.mmap

# Open a file
f = open('test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.read(10))

# Update content using slice notation;
# note that new content must have same size
m[6:11] = 'world'

# ... and read again using standard file methods
m.seek(0)
print(m.read(16))

# close the map
m.close()

# close the file
f.close()

# Test mmap.mmap

# Open a file
f = open('test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('
