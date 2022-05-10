import mmap
# Test mmap.mmap

# Create a file
f = open('test.txt', 'w+')
f.write('Hello world!')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
