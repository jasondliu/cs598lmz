import mmap
# Test mmap.mmap()
#
# This test is based on the example in the mmap documentation.

import os
import mmap

# Create a file and write a few lines to it
f = open('test.txt', 'w+')
f.write('Hello Python!\n')
f.write('Hello mmap!\n')
f.close()

# Open the file for reading
f = open('test.txt', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print 'First 10 bytes via read :', m.read(10)

# Read content via slice notation
print 'First 10 bytes via slice:', m[:10]

# Update content using slice notation;
# note that new content must have same size
m[6:] = 'world!\n'

# ... and read again using standard file methods
m.seek(0)
print 'First 10 bytes via read :', m.read(10)

# Close the map
m.close()

# Close the file
