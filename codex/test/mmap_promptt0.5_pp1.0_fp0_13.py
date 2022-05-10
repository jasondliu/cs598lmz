import mmap
# Test mmap.mmap()

# Open file in read-only mode
f = open('lorem.txt', 'r')

# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Print entire file
print(m.readline())

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file in read-write mode
f = open('lorem.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print(m.readline())

# Write to mmap
m.write(b'Hello Python!')
m.seek(0)

# Read from mmap
print(m.readline())

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

