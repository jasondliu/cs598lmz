import mmap
# Test mmap.mmap.read()

# Open file
fd = os.open('/tmp/mmap_test', os.O_RDWR | os.O_CREAT)

# Write a few bytes
os.write(fd, 'abcdefghijklmnop')

# Create mmap'ed file
m = mmap.mmap(fd, 16)

# Read a few bytes
