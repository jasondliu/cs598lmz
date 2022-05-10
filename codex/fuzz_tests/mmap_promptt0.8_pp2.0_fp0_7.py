import mmap
# Test mmap.mmap.write() on a read-only mapping
#

import mmap
import os
import unittest

def check_mmap_write(size, read_only):
    fn = "check_mmap_write.%s.%d" % (read_only and 'ro' or 'rw', size)
    f = file(fn, 'wb+')
    f.seek(size-1)
    f.write('\0')
    f.flush()
    f.seek(0)
    m = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_WRITE)
    if read_only:
        m.resize(size//2)
        m.close()
        f.close()
        f = file(fn, 'rb')
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        # XXX
        os.unlink(fn)
        return 0
    else:
        m.write('x')
        m.close()
        f.close()
