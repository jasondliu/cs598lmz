import mmap
# Test mmap.mmap.read() method

# Open file
f = open('test.txt', 'r')

# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read first 10 bytes
print m.read(10)

# Close the file
f.close()
