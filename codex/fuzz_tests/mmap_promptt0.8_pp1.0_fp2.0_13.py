import mmap
# Test mmap.mmap() with unusual offset/size parameters.

import sys, mmap

# Test a mmap created with offset that doesn't start at a page boundary.
# Note that the size we use here is larger than the file size.  For
# the non-Windows case, that's OK because the file size is rounded up
# to the next page boundary when mapping into memory (and there's no
# way to verify the rounded size on Windows).
SIZE = 65536
OFFSET = mmap.PAGESIZE + 1

print 'map size   :', SIZE
print 'map offset :', OFFSET
print 'page size  :', mmap.PAGESIZE

with open(mmap.__file__, "r+") as f:
    m = mmap.mmap(f.fileno(), SIZE, access=mmap.ACCESS_WRITE, offset=OFFSET)
    m.write(" ")
    m.flush()
    m.close()
