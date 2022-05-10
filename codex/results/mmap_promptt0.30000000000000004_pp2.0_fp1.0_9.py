import mmap
# Test mmap.mmap()

# Open a file
f = open('/tmp/foo.txt', 'w+')

# Write to the file
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('/tmp/foo.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print m.read(10)

# Close the memory-map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open a file
f = open('/tmp/foo.txt', 'w+')

# Write to the file
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('/tmp/foo.txt', 'r+')

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Move to the beginning of the memory-
