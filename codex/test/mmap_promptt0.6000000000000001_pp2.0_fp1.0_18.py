import mmap
# Test mmap.mmap(fileno, length, access=ACCESS_DEFAULT, offset=0)
#
# This test is designed to test the mmap function in the mmap module.

import os
import sys
import unittest
from test.support import TESTFN, unlink, run_unittest, cpython_only

class MmapTests(unittest.TestCase):

    def setUp(self):
        self.filename = TESTFN
        fp = open(self.filename, 'wb+')
        fp.write(b'\0' * 10000)
        fp.close()

    def tearDown(self):
        unlink(self.filename)

    def test_basic(self):
        size = os.path.getsize(self.filename)
        fp = open(self.filename, 'rb')
        m = mmap.mmap(fp.fileno(), size)
        fp.close()

        self.assertEqual(len(m), size)
        self.assertEqual(m[0], 0)
