import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/dev/urandom', os.O_RDONLY)
# Map file
buf = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)
# Get results
print(buf.read(10))
# Close file
os.close(fd)
</code>

