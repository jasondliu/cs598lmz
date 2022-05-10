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

# Read content via standard file methods
print m.readline()

# Read content via slice notation
print m[:5]

# Update content using slice notation;
# note that new content must have same size
m[6:] = 'world!'

# ... and read again using standard file methods
m.seek(0)
print m.readline()

# close the map
m.close()

# close the file
f.close()

# Test mmap.mmap()
#
# Create a file and write a few things to it
f = open('mmaptest.txt', 'w')
f.write('Hello Python!')
f.close
