import mmap
# Test mmap.mmap()

# Open a file for shared memory access
f = open('/dev/fmemshare', 'r+')

# Create a memory map to the file
m = mmap.mmap(f.fileno(), 1000000)

# Read the first few bytes
print(m.read(100))

# Write a few bytes
m.write('Hello Python!')

# Search for a string
print(m.find('Pytho'))

# Deactivate the memory map
m.close()

# Close the file
f.close()
