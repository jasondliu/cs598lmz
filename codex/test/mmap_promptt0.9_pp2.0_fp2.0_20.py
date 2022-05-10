import mmap
# Test mmap.mmap(fileno, length, tagname=None, access=ACCESS_DEFAULT, offset=0)

# Open an existing file for reading.
fd = os.open('/tmp/foo', os.O_RDWR)

# Memory-map the file.
m = mmap.mmap(fd, 0)

# Read from the memory-mapped file.
print(m.readline())    # prints "Hello Python!\n"

# Update the file from the memory-map.
# Note that the changes are made on the memory-mapped file.
m.seek(0)
m.write('Hello World!\n')

m.seek(0)
print(m.readline())    # prints "Hello World!\n"

# Close the memory-mapped file.
m.close()

# Close the file descriptor.
os.close(fd)
