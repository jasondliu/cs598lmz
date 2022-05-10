import mmap
# Test mmap.mmap

# Open the file
fd = os.open('/etc/passwd', os.O_RDONLY)
# Create the mmap
m = mmap.mmap(fd, 0)
# Print the contents
print m.read()
# Close the file
os.close(fd)
# Test mmap.mmap

# Open the file
fd = os.open('/etc/passwd', os.O_RDONLY)
# Create the mmap
m = mmap.mmap(fd, 0, prot=mmap.PROT_READ)
# Print the contents
print m.readline()
# Close the file
os.close(fd)
# Test mmap.mmap

# Open the file
fd = os.open('/etc/passwd', os.O_RDONLY)
# Create the mmap
m = mmap.mmap(fd, 0, prot=mmap.PROT_READ)
# Print the contents
print m[0:10]
# Close the file
os.close(fd)
# Test mmap.mmap

