import mmap
# Test mmap.mmap(0, 1)

import mmap
import os

# Create a file
f = open('test.txt', 'wb')
f.write(b'0123456789abcdef')
f.close()

# Open the file
f = open('test.txt', 'rb')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

# Print the content of the memory-mapped file
print(m.read(1))

# Update content using slice notation;
# note that new content must have same size
m[4:8] = b'AAAA'

# ... and read again using standard file methods
f.seek(0)
print(f.read(10))

# Close the map
m.close()

# Close the file
f.close()

# Clean up the file
