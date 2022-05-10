import mmap
# Test mmap.mmap()

# Open a file
fd = os.open('/tmp/test.txt', os.O_RDWR | os.O_CREAT)

# Create a memory-map to the file.  Size 0 means
# whole file, starting at offset 0.
m = mmap.mmap(fd, 0)

