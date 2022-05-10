import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.close()

# Open file
f = open('test.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.read(10))

# Update content using slice notation;
# note that new content must have same size
m[6:] = 'ABCDEF'

# ... and read again using standard file methods
m.seek(0)
print(m.read(10))

# Close the map
m.close()

# Close the file
f.close()

# Open file
f = open('test.txt', 'r+')

# Memory-map the file, size 0 means whole file, read-only
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read content via standard
