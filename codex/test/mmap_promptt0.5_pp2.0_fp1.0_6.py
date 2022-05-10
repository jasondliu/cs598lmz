import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+b')

# Memory-map file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

# Read content via standard file methods
print(m.readline())
print(m.readline())

# Re-set file offset to 8
m.seek(8)

# Write to file using mmap (note that new content must be same size)
m.write(b'0123456789abcdef')

# Close the map
m.close()

# Close the file
f.close()

# Open file
f = open('test.txt', 'r')

# Read content via standard file methods
print(f.readline())
print(f.readline())

# Close the file
f.close()

# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+b')

# Memory-map file, size 0 means whole file
m
