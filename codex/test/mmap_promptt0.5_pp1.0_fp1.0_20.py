import mmap
# Test mmap.mmap()

# Create file
f = open('test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

# Memory-map the file, size 0 means whole file
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Read contents
