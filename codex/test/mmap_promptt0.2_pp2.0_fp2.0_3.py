import mmap
# Test mmap.mmap

# Create a file
f = open('test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 16)

# Read content via standard file methods
print(f.read(16))

# Read content via mmap memory
print(m[:])

# Update content using slice notation;
# note that new content must have same size
m[4:8] = 'AAAA'

# ... and read again using standard file methods
f.seek(0)
print(f.read(16))

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap

# Create a file
f = open('test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

# Open the file
