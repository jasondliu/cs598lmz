import mmap
# Test mmap.mmap

# Create a file and write to it
f = open('test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
