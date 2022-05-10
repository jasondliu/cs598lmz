import mmap
# Test mmap.mmap

# Open a file
fd = os.open('/tmp/test.txt', os.O_RDWR | os.O_CREAT)

# Write a few bytes
os.write(fd, b'0123456789abcdef')

# Create a memory-map to the file
m = mmap.mmap(fd, 16)

# Read some data
print(m[4:8])

# Update data using slice notation;
# note that new data must have same size
# as slice
m[4:8] = b'AAAA'

# Read from position 0 thru position 10
print(m[:11])

# Close the memory-mapped file
m.close()

# Close the underlying file
os.close(fd)

# Test mmap.mmap

# Open a file
fd = os.open('/tmp/test.txt', os.O_RDWR | os.O_CREAT)

# Write a few bytes
os.write(fd, b'0123456789abcdef')

# Create a memory-map to
