import mmap
# Test mmap.mmap

# Open a file
f = open('/tmp/test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('/tmp/test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print(m[4:8])

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap

# Open a file
f = open('/tmp/test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('/tmp/test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print(m[4:8])

# Close the mmap object
