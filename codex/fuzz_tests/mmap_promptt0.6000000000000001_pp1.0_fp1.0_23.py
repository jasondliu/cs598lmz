import mmap
# Test mmap.mmap()

# Create a file and write some data to it
f = open('test.dat', 'wb')
f.write(b"Hello Python!\n")
f.close()

# Open the file for reading
f = open('test.dat', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-mapped file
print(m.readline())

# Close the map
m.close()
