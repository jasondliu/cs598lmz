import mmap
# Test mmap.mmap.read

import os, sys

if sys.platform == 'win32':
    print 'Test skipped on Windows'
    sys.exit(0)

size = 1024

with open('junk', 'w+') as f:
    f.write('\0' * size)

with open('junk', 'r+') as f:
    m = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_READ)
    assert m.read(10) == '\0' * 10
    assert m.read(size) == '\0' * size
    m.close()

with open('junk', 'r+') as f:
    m = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_WRITE)
    m.write('foo')
    assert m.read(3) == 'foo'
    m.close()

with open('junk', 'r+') as f:
    m = mmap.mmap(f.fileno(), size, access=mmap.
