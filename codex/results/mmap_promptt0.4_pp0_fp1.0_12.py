import mmap
# Test mmap.mmap()

# Create file
f = open('/tmp/test.txt', 'wb')
f.write('Hello World')
f.close()

# Open file
f = open('/tmp/test.txt', 'r+b')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content
print m.read(11)

# Close file
f.close()

# Delete file
os.remove('/tmp/test.txt')

# Test mmap.mmap()

# Create file
f = open('/tmp/test.txt', 'wb')
f.write('Hello World')
f.close()

# Open file
f = open('/tmp/test.txt', 'r+b')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content
print m.read(11)

# Write content
m.seek(0)
m.write('Goodbye World')

# Close file
f.close()

# Delete file

