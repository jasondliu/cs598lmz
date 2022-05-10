import mmap
# Test mmap.mmap

# Open a file
fd = os.open('test.dat', os.O_RDWR | os.O_CREAT)

# Create a memory-map to the file
m = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)

# Write to the memory-mapped file
m.write(b'Hello Python!')

# Close the memory-mapped file
m.close()

# Close the file
os.close(fd)

# Open a file
fd = os.open('test.dat', os.O_RDONLY)

# Create a memory-map to the file
m = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_READ)

# Read from the memory-mapped file
print(m.readline())

# Close the memory-mapped file
m.close()

# Close the file
os.close(fd)

# Delete the file
os.
