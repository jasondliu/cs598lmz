import mmap
# Test mmap.mmap()
#
# This test is designed to test the mmap.mmap() method.
#
# This test is designed to be run from the root directory of the project,
# as it imports the mmap module from the current directory.

import mmap
import os
import unittest

from test import support


class MmapTests(unittest.TestCase):
    def setUp(self):
        self.filename = support.TESTFN
        f = open(self.filename, 'wb+')
        try:
            f.write(b'\0' * mmap.ALLOCATIONGRANULARITY)
        finally:
            f.close()

    def tearDown(self):
        os.unlink(self.filename)

    def test_badargs(self):
        # Try invalid arguments to mmap.mmap()
        self.assertRaises(TypeError, mmap.mmap, 1, 2, 3, 4, 5, 6)
        self.assertRaises(TypeError, mmap.mmap, 1)
