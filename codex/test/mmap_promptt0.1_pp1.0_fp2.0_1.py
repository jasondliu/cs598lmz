import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/mmap_test', os.O_RDWR | os.O_CREAT)

# Zero out the file to lengthen it
assert os.write(fd, '\x00' * mmap.PAGESIZE) == mmap.PAGESIZE

# Create mmap'ed file
m = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)

