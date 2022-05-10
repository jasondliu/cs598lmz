import mmap
# Test mmap.mmap.read()

# Open file
fd = os.open('/tmp/mmap_test', os.O_RDWR | os.O_CREAT)

# Write a few bytes
os.write(fd, 'abcdefghijklmnop')

# Create mmap'ed file
m = mmap.mmap(fd, 16)

# Read a few bytes
print m.read(1)
print m.read(5)

# Close file
os.close(fd)

# Close mmap'ed file
m.close()

# Remove file
os.unlink('/tmp/mmap_test')
