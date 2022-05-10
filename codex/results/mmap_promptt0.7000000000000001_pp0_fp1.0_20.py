import mmap
# Test mmap.mmap(-1, 0) to make sure the file descriptor is closed.
# This should not crash.
mmap.mmap(-1, 0)

import mmap
import os
try:
    mmap.mmap(os.open(__file__, os.O_RDONLY), 0)
    raise Exception('expected an exception')
except Exception:
    pass

import mmap
import os
try:
    mmap.mmap(os.open(__file__, os.O_RDONLY), 0, access=mmap.ACCESS_COPY)
    raise Exception('expected an exception')
except Exception:
    pass

import mmap
import os
try:
    mmap.mmap(os.open(__file__, os.O_RDONLY), 0, access=mmap.ACCESS_WRITE)
    raise Exception('expected an exception')
except Exception:
    pass

import mmap
import os
try:
    mmap.mmap(os.open(__file__, os.O_RDONLY), 0, access=mmap
