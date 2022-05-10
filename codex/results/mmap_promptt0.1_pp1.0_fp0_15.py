import mmap
# Test mmap.mmap()
#
# This test is based on the example in the mmap module documentation.
#
# The test file is created in the current directory.

import mmap
import os
import unittest

from test import support

TESTFN = support.TESTFN

class MmapTests(unittest.TestCase):

    def setUp(self):
        fp = open(TESTFN, 'w+b')
        fp.write(b'\0' * mmap.ALLOCATIONGRANULARITY)
        fp.close()

    def tearDown(self):
        support.unlink(TESTFN)

    def test_basic(self):
        size = mmap.ALLOCATIONGRANULARITY
        fp = open(TESTFN, 'r+b')
        m = mmap.mmap(fp.fileno(), size)
        self.assertEqual(len(m), size)
        self.assertEqual(m.size(), size)
        self.assertEqual(m.tell(), 0)
        self.assert
