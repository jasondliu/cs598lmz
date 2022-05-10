import mmap
# Test mmap.mmap()

# Open a file
fd = os.open("foo.txt", os.O_RDWR)

# Memory-map the file, size 0 means whole file
m = mmap.mmap(fd, 0)
