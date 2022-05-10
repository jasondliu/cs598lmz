import mmap
# Test mmap.mmap

# Create a file and write a few things to it
f = open('test.txt', 'w')
f.write('Hello Python!')
f.write('Bye bye Python!')
f.close()

# Open the file for reading
f = open('test.txt', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from the mmap
