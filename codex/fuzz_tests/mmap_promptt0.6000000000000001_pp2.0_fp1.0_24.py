import mmap
# Test mmap.mmap()

# Open file
f = open('/dev/zero', 'r')
# Create memory-map of file
mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)

# Print the first ten bytes
print mm.read(10)

# Close file
f.close()

# Unmap the memory
mm.close()
