import mmap
# Test mmap.mmap()

# Open file
f = open('/home/matt/Desktop/Python/test.txt', 'r+')

# Memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)
# Read content via standard file methods
print mm.readline()  # prints "Hello Python!"

# Update content using slice notation;
# note that new content must have same size
mm[6:] = 'world'

# ... and read again using standard file methods
mm.seek(0)
print mm.readline()  # prints "Hello world!"

# close the map
mm.close()

# close the file
f.close()

# Test mmap.mmap()

# Open file
f = open('/home/matt/Desktop/Python/test.txt', 'r+')

# Memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)
# Read content via standard file methods
print mm.readline()  # prints "Hello Python!"


