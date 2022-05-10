import mmap
# Test mmap.mmap

# Open file for reading
f = open('lorem.txt', 'r+')

# Create mmap starting at page 0, size 5242880 bytes
m = mmap.mmap(f.fileno(), 5242880)

# Read from mmap
print m.readline()

# Close mmap
m.close()

# Close file
f.close()

# Open file for reading
f = open('lorem.txt', 'r+')

# Create mmap starting at page 0, size 5242880 bytes
m = mmap.mmap(f.fileno(), 5242880)

# Read from mmap
print m.readline()

# Close mmap
m.close()

# Close file
f.close()

# Open file for reading
f = open('lorem.txt', 'r+')

# Create mmap starting at page 0, size 5242880 bytes
m = mmap.mmap(f.fileno(), 5242880)

# Read from mmap
print m.readline()
