import mmap
# Test mmap.mmap.read()

# Create a file and write some data
with open('test.dat', 'wb') as f:
    f.write(b'0123456789abcdef')

# Open the file for reading
with open('test.dat', 'rb') as f:
    # Memory-map the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # Read some data
    print(m.read(10))
    # Close the map
    m.close()

# Open the file for reading
with open('test.dat', 'rb') as f:
    # Memory-map the file, size 0 means whole file, read-only
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # Read the file
    print(m[:])
    # Close the map
    m.close()

# Open the file for reading
