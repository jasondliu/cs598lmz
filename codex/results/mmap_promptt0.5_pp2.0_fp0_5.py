import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test.txt', 'r+b')

# Zero out the file
f.seek(0)
f.write(b'\x00' * mmap.ALLOCATIONGRANULARITY)
f.flush()

# Create mmap'ed file
m = mmap.mmap(f.fileno(), mmap.ALLOCATIONGRANULARITY, access=mmap.ACCESS_WRITE)

# Write to the file
m.write(b'abcdef')
m.flush()

# Read from the file
m.seek(0)
print(m.read(6))

# Close the mmap
m.close()

# Close the file
f.close()

# Test mmap.mmap() with offset

# Open file
f = open('/tmp/test.txt', 'r+b')

# Zero out the file
f.seek(0)
f.write(b'\x00' * mmap.ALLOCATIONGRANULARITY)
f.flush()

