import mmap
# Test mmap.mmap

# Open file
f = open('/tmp/test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.close()

# Open file
f = open('/tmp/test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read from file via memory map
