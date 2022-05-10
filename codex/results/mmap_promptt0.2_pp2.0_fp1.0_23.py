import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/mmap_test', 'w+')

# Write some data
f.write('Hello Python!')

# Close the file
f.close()

# Open the file
f = open('/tmp/mmap_test', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print m.readline()

# Close the mmap object
m.close()

# Close the file
f.close()

# Delete the file
os.remove('/tmp/mmap_test')

# Test mmap.mmap()

# Open file
f = open('/tmp/mmap_test', 'w+')

# Write some data
f.write('Hello Python!')

# Close the file
f.close()

# Open the file
f = open('/tmp/mmap_test', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0
