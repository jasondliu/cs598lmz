import mmap
# Test mmap.mmap()

# Open a file
f = open('/tmp/test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Print the content via the memory-mapped file
print(m.readline())

# Close the memory-mapped file
m.close()

# Close the underlying file
f.close()

# Test mmap.mmap()

# Open a file
f = open('/tmp/test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read the content via the memory-mapped file
print(m[:])

# Close the memory-mapped file
m.close()

# Close the underlying file
f.close()

# Test mmap.mmap()

# Open a file
f = open('/tmp/test.txt', 'r+')

# Create a memory-
