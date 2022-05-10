import mmap
# Test mmap.mmap(0, length, access=mmap.ACCESS_WRITE)

import os
import sys

if sys.platform == 'darwin':
    print('Test skipped: the mmap module is not available on Mac OS X')
    sys.exit(0)

try:
    mmap.mmap(0, 1)
except ValueError:
    print('Test skipped: the mmap module is not available on this system')
    sys.exit(0)

# create a file and write a few bytes to it
f = open('foo', 'wb+')
f.write(b'0123456789abcdef' * 16)
f.flush()

# try to map the whole file
m = mmap.mmap(f.fileno(), 0)
m.close()
f.close()

# try to map a section of the file
f = open('foo', 'rb+')
m = mmap.mmap(f.fileno(), 16, access=mmap.ACCESS_WRITE)
m.close()
f.close()

# try to map
