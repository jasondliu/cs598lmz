import mmap
# Test mmap.mmap()

# Open a file
f = open('/tmp/mmaptest.txt', 'r+b')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Print the file
print m.readline()

# Update the file
m.seek(0)
m.write('0123456789abcdef')

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open a file
f = open('/tmp/mmaptest.txt', 'r+b')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Print the file
print m.readline()

# Update the file
m.seek(0)
m.write('0123456789abcdef')

# Close the map
m.close()

# Close the file
f.close()

# Test mmap
