import mmap
# Test mmap.mmap()

# Create the file
f = open('test.dat', 'w+')

# Write the data
f.write('0123456789abcdef' * 1024 * 1024 * 10)
f.close()

# Open the file
f = open('test.dat', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print m.read(10)

# Read content via slice notation
print m[:10]

# Update content using slice notation;
# note that new content must have same size
m[6:11] = 'abcde'

# ... and read again using standard file methods
m.seek(0)
print m.read(10)

# close the map
m.close()

# close the file
f.close()

# Test mmap.mmap()

# Create the file
f = open('test.dat', 'w+')

# Write the data
f.write('01234567
