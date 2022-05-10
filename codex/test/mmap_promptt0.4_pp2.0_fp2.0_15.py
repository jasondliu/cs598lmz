import mmap
# Test mmap.mmap.read_byte()
# https://docs.python.org/2/library/mmap.html

# Create a file
f = open('test.txt', 'wb')
f.write('Hello Python!')
f.close()

# Open a file
f = open('test.txt', 'r+')

# Map file to memory
m = mmap.mmap(f.fileno(), 0)

