import mmap
# Test mmap.mmap()
# Open file
f = open('/dev/urandom', 'rb')
# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# Print the first 10 bytes
print m[:10]
# Close file and mmap object
m.close()
f.close()

# Test mmap.mmap()
# Open file
f = open('/dev/urandom', 'rb')
# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# Print the first 10 bytes
print m[:10]
# Close file and mmap object
m.close()
f.close()
