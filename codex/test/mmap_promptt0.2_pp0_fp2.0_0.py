import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.seek(0)

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.read(10))
print(m.read(1))
print(m.readline())

# Update content using slice notation;
# note that new content must have same size
m[4:8] = 'AAAA'

# ... and read again using standard file methods
m.seek(0)
print(m.read(10))

# close the map
m.close()

# close the file
f.close()

# Test mmap.mmap

# Open file
f = open('test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.seek(0)

