import mmap
# Test mmap.mmap()

# Create file
with open('lorem.txt', 'w') as f:
    f.write('Hello world')

# Open file
f = open('lorem.txt', 'r+')
# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# Read content via standard file methods
