import mmap
# Test mmap.mmap

# Create a memory-mapped file, size 0
m = mmap.mmap(-1, 0)

# Write a simple message at the start of memory-mapped file
m.write("Hello Python!\n")

# Move the file position indicator to the start of the file
m.seek(0)

# Read the entire content of the memory-mapped file
print m.readline()

# Close the memory-mapped file
m.close()
