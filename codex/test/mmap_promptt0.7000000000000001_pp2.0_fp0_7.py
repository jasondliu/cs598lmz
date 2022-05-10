import mmap
# Test mmap.mmap(fileno, length, ...)
#
# Note that mmap.mmap(..., access=mmap.ACCESS_COPY) is a read-only
# mapping. However, it is dependent on the underlying file being
# opened in read-write mode.
#
# XXX Do we want to test mmap.mmap(-1, ...) ?
#

# --------------------------------------------------------------------

import os
import mmap
import unittest
import tempfile
import array

class MmapTests(unittest.TestCase):
    def setUp(self):
        # create empty file
        fd, self.fname = tempfile.mkstemp()
        os.close(fd)

    def tearDown(self):
        # remove empty file
        try:
            os.unlink(self.fname)
        except OSError:
            pass

