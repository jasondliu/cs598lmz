import mmap
# Test mmap.mmap(-1, length, access=mmap.ACCESS_WRITE),
# Where length is the size of the file.
# Use os.open to open the file, specify that it is to be created if it
# doesn't exist and that it is readable and writable.
#
# With this method, the file doesn't need to be pre-allocated,
# and no special flags are needed to create a sparse file.

import os
import mmap

length = 100 * 1024 * 1024
# length = 1

if os.path.exists('data'):
    os.unlink('data')

fd = os.open('data', os.O_RDWR | os.O_CREAT)

# Zero out the first (length) bytes of the file.
os.write(fd, b'\x00' * length)

m = mmap.mmap(fd, length, access=mmap.ACCESS_WRITE)

# Write 1 to the 10th byte.
m[9] = b'\x01'

m.close()
