import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'w+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Write to mmap
m.write('Hello world!')

# Close file
f.close()

# Open file
f = open('/tmp/test.txt', 'r')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print(m.read(11))

# Close file
f.close()

# Delete file
os.remove('/tmp/test.txt')

# Open file
f = open('/tmp/test.txt', 'w+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Write to mmap
m.write('Hello world!')

# Move to beginning of file
m.seek(0)

# Read from mmap
print(m.read(11))

# Close file
