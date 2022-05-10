import mmap
# Test mmap.mmap()

# Test mmap.mmap()
data = "Hello mmap world"

# Open file for writing
f = open('mmap.txt', 'w+')
print f.write(data)

# Open file for reading
f = open('mmap.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from mmap
print m.readline()

# Close mmap
m.close()

# Close file
f.close()

# Open file for writing
f = open('mmap.txt', 'w+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

# Write to mmap
print m.write("Hello mmap world")

# Close mmap
m.close()

# Close file
f.close()
