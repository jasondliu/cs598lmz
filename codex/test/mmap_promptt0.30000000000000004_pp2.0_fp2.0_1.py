import mmap
# Test mmap.mmap()

# Open file for reading
f = open('lorem.txt', 'r')

# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Print entire file
