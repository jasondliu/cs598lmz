import mmap
# Test mmap.mmap(0,1)
# This is only for the case where mmap.ALLOCATIONGRANULARITY is greater than 1.

import mmap
import os
import unittest

# This is the only way I can find to determine the allocation granularity.
# It's not documented, but it's in the source code.
PAGESIZE = mmap.ALLOCATIONGRANULARITY

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.filename = test.support.TESTFN
        f = open(self.filename, 'wb+')
        f.write(b'\0' * PAGESIZE)
        f.close()

    def tearDown(self):
        os.unlink(self.filename)

    def test_anonymous_zero(self):
        # Issue #1764703: mmap.mmap(0,1) failed when ALLOCATIONGRANULARITY > 1
        m = mmap.mmap(0, 1)
        self.assertEqual(len(m), 1)
        self.
