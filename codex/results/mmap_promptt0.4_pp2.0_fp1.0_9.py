import mmap
# Test mmap.mmap()

# Open a file
fd = os.open('test.txt', os.O_RDWR)

# Memory-map the file, size 0 means whole file
m = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)

# Print content
print m[:]

# Write a new line at the end of the file
m.seek(0, os.SEEK_END)
m.write("\nHello, Python!\n")

# Print the file again
m.seek(0)
print m[:]

# Close the map
m.close()

# Close the file
os.close(fd)

# Test mmap.mmap()

# Open a file
fd = os.open('test.txt', os.O_RDWR)

# Memory-map the file, size 0 means whole file
m = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)

# Print content
print m[:]

# Write a new line at the end of the file
m.
