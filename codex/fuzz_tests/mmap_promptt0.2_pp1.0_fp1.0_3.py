import mmap
# Test mmap.mmap()
#
# This test is a bit tricky because we want to test the mmap module's
# mmap() function, but we can't use the mmap() function to test itself.
# To get around this, we use the os module's open() function to open
# the mmap module's __file__ attribute, and then use the mmap module's
# mmap() function to map that file.  We can then use the mmap object's
# methods to test the mmap module's mmap() function.

import os
import mmap

# Open the mmap module's __file__ attribute for reading.
f = os.open(mmap.__file__, os.O_RDONLY)

# Map the file.
m = mmap.mmap(f, 0, access=mmap.ACCESS_READ)

# Read the first line of the file.
s = m.readline()

# Close the file.
m.close()
os.close(f)

# Make sure the first line of the file is what we expect.
assert s.startswith('#
