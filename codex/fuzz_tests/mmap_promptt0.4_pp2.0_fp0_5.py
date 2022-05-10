import mmap
# Test mmap.mmap()

# Open file and memory-map it
fp = open('/etc/passwd', 'r')
m = mmap.mmap(fp.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)

# Read the first line of the file
line = m.readline()
print('First line:', line)

# Read the entire file
all_data = m.read()
print('All data:', all_data)

# Close the map and the file
m.close()
fp.close()

# Test mmap.mmap()

# Open file and memory-map it
fp = open('/etc/passwd', 'r')
m = mmap.mmap(fp.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)

# Read the first line of the file
line = m.readline()
print('First line:', line)

# Read the entire file
all_data = m.read()
print('All data:', all_data)

#
