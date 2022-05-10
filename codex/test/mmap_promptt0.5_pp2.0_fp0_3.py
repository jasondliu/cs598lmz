import mmap
# Test mmap.mmap.__init__

import mmap
import os
import unittest

from test import support

TESTFN = support.TESTFN

# A simple test for mmap.mmap.__init__.

class MmapTestCase(unittest.TestCase):
    def setUp(self):
        f = open(TESTFN, 'wb+')
        try:
            f.write(b'\0' * 1024)
        finally:
            f.close()

    def tearDown(self):
        support.unlink(TESTFN)

    def test_init(self):
        # mmap.mmap.__init__
        f = open(TESTFN, 'r+b')
        m = mmap.mmap(f.fileno(), 1024)
        f.close()
        self.assertEqual(m.size(), 1024)
        m.close()

        m = mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_READ)
