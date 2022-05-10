import mmap
# Test mmap.mmap()
#
# This test is based on the example in the mmap documentation.
#
# The test file is created with the following Python script:
#
#   f = open("mmaptest", "w+")
#   for i in range(10):
#       f.write("ABCDEFGHIJ"*1024)
#   f.close()
#
# The test file is 10240 bytes long.

import unittest
import os
import mmap

from test import test_support

class MmapTests(unittest.TestCase):
    def setUp(self):
        f = open(test_support.TESTFN, "w+")
        try:
            f.write("ABCDEFGHIJ"*1024)
        finally:
            f.close()

    def tearDown(self):
        os.unlink(test_support.TESTFN)

    def test_basic(self):
        size = os.path.getsize(test_support.TESTFN)
        f = open(test_support.TESTFN, "r+")

