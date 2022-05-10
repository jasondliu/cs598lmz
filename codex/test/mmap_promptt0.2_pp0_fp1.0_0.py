import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.seek(0)

# Create memory-map
m = mmap.mmap(f.fileno(), 16)

# Read from file via memory-map
