import mmap
# Test mmap.mmap

import mmap

# Open file
f = open('test.txt', 'r+')

# Memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)
# Read content via standard file methods
print(mm.readline())  # prints "Hello Python!"

# Update content using slice notation;
# note that new content must have same size
mm[6:13] = 'world'

# ... and read again using standard file methods
mm.seek(0)
print(mm.readline())  # prints "Hello world!"

# close the map
mm.close()

# close the file
f.close()

# Test mmap.ACCESS_READ
import mmap

# Open file
f = open('test.txt', 'r+')
# Memory-map the file, size 0 means whole file, read-only
mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# Read content via standard file methods
print(mm.readline())  #
