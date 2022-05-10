import mmap
# Test mmap.mmap()

# Create the file
f = open('test.dat', 'w+')

# Write the data
f.write('0123456789abcdef' * 1024 * 1024 * 10)
f.close()

# Open the file
f = open('test.dat', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
