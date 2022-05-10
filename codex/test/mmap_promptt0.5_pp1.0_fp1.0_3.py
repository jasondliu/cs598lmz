import mmap
# Test mmap.mmap()
# Open file for reading
f = open('/etc/passwd', 'r')
# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# Print entire file
print(m.readline())
# Close the mmap object
m.close()
# Close the file
f.close()

# Test mmap.mmap()
# Open file for reading
f = open('/etc/passwd', 'r')
# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# Print entire file
print(m.readline())
# Close the mmap object
m.close()
# Close the file
f.close()

# Test mmap.mmap()
# Open file for reading
f = open('/etc/passwd', 'r')
# Create mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# Print entire file
