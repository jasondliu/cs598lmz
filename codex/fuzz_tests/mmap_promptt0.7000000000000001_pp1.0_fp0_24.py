import mmap
# Test mmap.mmap()

# This is an example of using mmap to create a memory-mapped file. 
# To use, run this program and then start a separate Python interpreter 
# and do 'import mmap_example'.  The separate interpreter will share the 
# same mmap object.  Note that you can only have one open file mapped 
# at a time for a given process.

import mmap
import sys

# Windows
# file_name = r"c:\temp\test.txt"

# Mac
file_name = "/tmp/test.txt"

size = len(open(file_name, 'rb').read())

# Create a memory-map to an integer array.
# Default value for access=mmap.ACCESS_WRITE
# mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

# Create a memory-map to a file on disk.
# Default value for access=mmap.ACCESS_WRITE
mm = mmap.mmap(
    -1, 
    size, 
    access
