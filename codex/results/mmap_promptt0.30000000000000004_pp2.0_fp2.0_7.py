import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/mmap_test', 'w+')

# Write data
f.write("Hello World")

# Close the file
f.close()

# Open file
f = open('/tmp/mmap_test', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read data
print m.readline()

# Close the memory map
m.close()

# Close the file
f.close()

# Delete file
os.remove('/tmp/mmap_test')

# Test mmap.mmap()

# Open file
f = open('/tmp/mmap_test', 'w+')

# Write data
f.write("Hello World")

# Close the file
f.close()

# Open file
f = open('/tmp/mmap_test', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read data
print m.readline
