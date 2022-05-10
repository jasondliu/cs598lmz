import mmap
# Test mmap.mmap()
#
# This test is derived from the test for mmap.mmap() in the standard
# library test suite.

import os
import mmap
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Check that mmap doesn't segfault when the file is smaller than the
# requested mapping size.

class MmapTests(unittest.TestCase):
    def setUp(self):
        fp = open(TESTFN, 'wb+')
        try:
            fp.write(b'\0' * 1024)
        finally:
            fp.close()

    def tearDown(self):
        support.unlink(TESTFN)

    def test_read_past_end(self):
        size = os.path.getsize(TESTFN)
        fp = open(TESTFN, 'rb')
