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

# Update content using mmap
m[4:8] = 'AAAA'

# Flush changes
m.flush()

# Close the map
m.close()

# See the modification
f = open('test.txt', 'r+')
print(f.read(16))

# Close the file
f.close()

# Cleanup
os.remove('test.txt')

# Test mmap.mmap

# Create a file
f = open('test.txt', 'w+')
