import mmap
# Test mmap.mmap()
#
# This test is based on the example in the mmap documentation.

import mmap
import os
import stat
import tempfile

# Create a temporary file and write some data to it
f = tempfile.TemporaryFile()
f.write(b"Hello world!\n")
f.flush()

# Re-open the file with mmap
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Print the content of the file
print(m.readline())

# Close the map and the file
m.close()
f.close()

# Create a temporary file and write some data to it
f = tempfile.TemporaryFile()
f.write(b"Hello world!\n")
f.flush()

# Re-open the file with mmap
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Print the content of the file
print(m.readline())

# Close the map and the file
m.close
