import mmap
# Test mmap.mmap()
#
# This test is based on the example in the mmap module documentation.
#
# The test file is created in the current directory.

import os
import mmap

# Create a file and write a few lines to it.
f = open('mmaptest.dat', 'w+')
f.write('Hello Python!\n')
f.write('Hello mmap!\n')
f.close()

# Open the file for reading.
f = open('mmaptest.dat', 'r')

# Create a mmap'ed file that is writable.
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

# Print the original contents.
print 'Original contents:', m.readline(),
print m.readline()

# Move to the beginning of the mmap'ed file.
m.seek(0)

# Overwrite the first line.
m.write('Hello world!\n')

# Read the modified contents.
m.seek(0)
print 'Modified contents:',
