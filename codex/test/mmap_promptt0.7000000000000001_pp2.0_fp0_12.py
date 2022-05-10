import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/dev/urandom', os.O_RDONLY)
# Map file
