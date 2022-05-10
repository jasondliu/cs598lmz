import mmap
# Test mmap.mmap(fileno, length, access=ACCESS_DEFAULT, offset=0)
#
# This test is based on the mmap module test.
#
# This test is not complete.

import mmap
import os
import unittest
import struct
import sys
import test.support

TESTFN = test.support.TESTFN

# Check that mmap is available on this platform.
try:
    mmap.mmap(0, 0)
except (ValueError, EnvironmentError):
    raise unittest.SkipTest("cannot mmap")

class MmapTests(unittest.TestCase):
    def setUp(self):
        fp = open(TESTFN, 'wb+')
        fp.write(b'\0' * 1024)
        fp.close()
        self.fp = open(TESTFN, 'rb+')

    def tearDown(self):
        self.fp.close()
        os.unlink(TESTFN)

