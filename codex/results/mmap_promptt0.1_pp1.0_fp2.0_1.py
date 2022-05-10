import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/mmap_test', os.O_RDWR | os.O_CREAT)

# Zero out the file to lengthen it
assert os.write(fd, '\x00' * mmap.PAGESIZE) == mmap.PAGESIZE

# Create mmap'ed file
m = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)

# Close the original fd
os.close(fd)

# Print initial buffer
print 'Before:', repr(m.read(mmap.PAGESIZE))

# Modify the buffer
m[0:11] = 'Hello World'
m.flush()

# Print modified buffer
print 'After :', repr(m.read(mmap.PAGESIZE))

# Close the mmap'ed file
m.close()

# Open the file for reading
fd = os.open('/tmp/mmap_test', os.O_RDONLY)

