import mmap
# Test mmap.mmap()
#
# Create a file for testing
file = open('mmap_file', 'w+')
file.write('\0' * 1024)
file.close()

# Open the file
file = open('mmap_file', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(file.fileno(), 0)
