import mmap
# Test mmap.mmap()

# Open file
f = open('/etc/passwd', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read
print m.readline()
print m.readline()
print m.readline()

# Close
m.close()

# Close file
f.close()

print '*' * 40

# Test mmap.mmap() with offset and length

# Open file
f = open('/etc/passwd', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)

# Read
print m[0:10]
print m[0:11]
print m[10:20]

# Close
m.close()

# Close file
f.close()

print '*' * 40

# test mmap.mmap() with size

# Open file
f = open('/etc/passwd', 'r+')
