import mmap
# Test mmap.mmap and mmap.ACCESS_READ

import mmap
import os
import unittest
from test import support

TESTFN = support.TESTFN

class MmapTests(unittest.TestCase):

    def setUp(self):
        # Create a file to be mmap'ed.
        with open(TESTFN, "wb") as f:
            f.write(b"\0" * mmap.ALLOCATIONGRANULARITY)

    def tearDown(self):
        support.unlink(TESTFN)

    def test_init(self):
        size = mmap.ALLOCATIONGRANULARITY
        with open(TESTFN, "r+b") as f:
            m = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_READ)
            self.assertEqual(len(m), size)
            self.assertEqual(m[0], 0)
            self.assertEqual(m[0:1], b"\0")
            m.close()

            m = mm
