import mmap
# Test mmap.mmap.resize() by creating a file and mmapping it and then resizing it
#  and verifying that the mapping is updated.

import os
import tempfile
import mmap

if not hasattr(mmap.mmap, 'resize'):
    print('mmap.resize not available... skipping test')
    exit(0)

# create empty file
fname = tempfile.mktemp()
file = open(fname, 'w+b')

# create and close mmap
m = mmap.mmap(file.fileno(), 0)
m.close()

# enlarge file by 20 bytes
file = open(fname, 'a')
file.write('Z' * 20)
file.close()

# reopen and resize mmap
m = mmap.mmap(file.fileno(), 0)
m.resize(20)
m.close()

# cleanup
os.unlink(fname)
