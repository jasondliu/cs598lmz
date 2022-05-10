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
