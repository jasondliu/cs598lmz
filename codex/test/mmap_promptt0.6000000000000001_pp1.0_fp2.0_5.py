import mmap
# Test mmap.mmap(fd, length)

# Create file
with open('testfile.txt', 'w') as f:
    f.write('Hello, world!')

# Open file
f = open('testfile.txt', 'r+')

# Create memory-mapped file
m = mmap.mmap(f.fileno(), 13)

# Read from file
