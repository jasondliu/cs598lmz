import mmap
# Test mmap.mmap()

# Create a string
str = '0123456789'

# Open a file
fd = os.open('data.txt', os.O_RDWR | os.O_CREAT)

# Write the string to the file
os.write(fd, str)

# Close the file descriptor
os.close(fd)

# Re-open the file
fd = os.open('data.txt', os.O_RDWR)

# Create a memory-map to the file
m = mmap.mmap(fd, len(str), access=mmap.ACCESS_WRITE)

# Print the original contents
print m.read(len(str))

# Update the contents
m[4] = '4'
m[6:8] = '67'

# Print the updated contents
print m.read(len(str))

# Close the map and the file
m.close()
os.close(fd)

# Create a string
str = '0123456789'

# Open a file
fd = os.open('data.
