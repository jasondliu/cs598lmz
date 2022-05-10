import mmap
# Test mmap.mmap()

# Create a file and write a line of text to it
f = open('myfile', 'w')
f.write('hello world\n')
f.close()

# Open the file for reading
f = open('myfile', 'r')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read the content via standard file methods
