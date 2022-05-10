import mmap
# Test mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE, access=ACCESS_DEFAULT)

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read file
print(m.readline())

# Close file
f.close()

# Close mmap
m.close()

# Test mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE, access=ACCESS_DEFAULT)

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read file
print(m.readline())

# Close file
f.close()

# Close mmap
m.close()

# Test mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE, access=ACCESS_
