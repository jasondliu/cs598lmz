import mmap
# Test mmap.mmap

# Open a file and map it into memory
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Print the file
