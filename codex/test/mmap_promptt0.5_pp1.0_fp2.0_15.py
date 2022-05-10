import mmap
# Test mmap.mmap()

# Create the file.
f = open('tmp', 'w+b')

# Write some data.
f.write(b'\x00' * mmap.PAGESIZE)

# Create the map.
m = mmap.mmap(f.fileno(), mmap.PAGESIZE, access=mmap.ACCESS_WRITE)

# Read from the map.
print(m[0:5])

# Close the map.
m.close()

# Close the file.
f.close()

# Test mmap.mmap()

# Create the file.
f = open('tmp', 'w+b')

# Write some data.
f.write(b'\x00' * mmap.PAGESIZE)

# Create the map.
m = mmap.mmap(f.fileno(), mmap.PAGESIZE, access=mmap.ACCESS_WRITE)

# Read from the map.
print(m[0:5])

# Close the map.
m.close()
