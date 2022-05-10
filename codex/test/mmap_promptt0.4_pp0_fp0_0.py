import mmap
# Test mmap.mmap()

# Create a memory-map to a file, and close the file
f = open('bigfile', 'w+')
f.write('\x00' * 10000000)
f.close()
m = mmap.mmap(f.fileno(), 10000000)

# Read the content via standard file methods
