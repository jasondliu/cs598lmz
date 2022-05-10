import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/mmaptest', 'w+')

# Write to file
f.write('Hello Python!')
f.close()

# Open file for reading
f = open('/tmp/mmaptest', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read from memory map
print m.readline()

# Close map
m.close()

# Close file
f.close()

# Test mmap.mmap()

# Open file
f = open('/tmp/mmaptest', 'w+')

# Write to file
f.write('Hello Python!')
f.close()

# Open file for reading
f = open('/tmp/mmaptest', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read from memory map
print m.readline()

# Close map
m.close()

# Close file
f.close()

# Test
