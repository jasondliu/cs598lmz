import mmap
# Test mmap.mmap

# Open a file
fd = os.open('test.txt', os.O_RDWR)

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(fd, 0)

# Print the file
print(m.readline())

# Close the map
m.close()

# Close the file
os.close(fd)

# Open a file
fd = os.open('test.txt', os.O_RDWR)

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(fd, 0)

# Read only part of the file
print(m[:5])

# Close the map
m.close()

# Close the file
os.close(fd)

# Open a file
fd = os.open('test.txt', os.O_RDWR)

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(fd, 0)

# Read only part of the file
print(m[
