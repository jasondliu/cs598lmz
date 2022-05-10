import mmap
# Test mmap.mmap()
#
# Create a file and write a few things to it
f = open('mmaptest.txt', 'w')
f.write('Hello Python!')
f.close()

# Open the file for reading
f = open('mmaptest.txt', 'r')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

