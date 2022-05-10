import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'w+')

# Write to file
f.write('Hello World!')
f.close()

# Open file
f = open('/tmp/test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read file
print(m[:])

# Update content using slice notation
# Note: new content must have same size
m[6:] = 'WORLD'

# See content change
m.seek(0)
print(m.readline())

# Close map
m.close()

# Close file
f.close()

# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'w+')

# Write to file
f.write('Hello World!')
f.close()

# Open file
f = open('/tmp/test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.
