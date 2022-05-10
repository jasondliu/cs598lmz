import mmap
# Test mmap.mmap(0, 1, access=mmap.ACCESS_WRITE)
# This should fail with ENOENT
#
# This test is not run by default.  To run it, do:
#     python -m test.mmap_test
#
# Note that this test is not thread safe and will crash if another thread
# creates a file named '@test' in the current directory.
import unittest
from test import support

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.filename = support.TESTFN

    def tearDown(self):
        support.unlink(self.filename)

