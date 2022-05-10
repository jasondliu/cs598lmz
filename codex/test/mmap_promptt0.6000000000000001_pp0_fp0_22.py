import mmap
# Test mmap.mmap with a file that is larger than 2 GB.

with open('bigfile', 'wb') as f:
    f.write(b'\x00' * 4 * 1024 * 1024 * 1024)

with open('bigfile', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

assert m.size() == 4 * 1024 * 1024 * 1024
m.close()

import os
os.unlink('bigfile')
