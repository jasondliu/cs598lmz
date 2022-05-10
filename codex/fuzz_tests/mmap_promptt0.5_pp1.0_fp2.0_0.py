import mmap
# Test mmap.mmap()

# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])

# Create a memory-mapped file object

import os
import mmap

# Create a file
file_name = 'test.txt'
f = open(file_name, 'w+')

f.write('''Hello World!''')
f.close()

# Open the file
f = open(file_name, 'r+')

# Memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(mm.readline())

# Update content using file's write method
mm.seek(0)
mm.write(b'That\'s cool!')

# Close the map
mm.close()

# Close the file
f.close()

# Test mmap.mmap()

# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])

# Create
