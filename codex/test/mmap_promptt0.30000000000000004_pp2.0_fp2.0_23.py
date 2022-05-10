import mmap
# Test mmap.mmap()

# Create a file
f = open('test', 'w+')
f.write("Hello world")
f.close()

# Open the file in read-only mode
f = open('test', 'r')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Print the content via standard file methods
