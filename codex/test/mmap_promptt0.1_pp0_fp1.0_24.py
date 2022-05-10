import mmap
# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 16)

# Read content via standard file methods
