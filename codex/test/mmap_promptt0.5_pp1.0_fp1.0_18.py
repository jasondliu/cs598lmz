import mmap
# Test mmap.mmap

# Open the file
fd = os.open('/etc/passwd', os.O_RDONLY)
# Create the mmap
m = mmap.mmap(fd, 0)
