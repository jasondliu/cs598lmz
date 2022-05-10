import mmap
# Test mmap.mmap
import random
import time
import zipfile
import contextlib
import sys

if sys.platform.startswith('java'):
    from . import py26_test_support as support
else:
    from test import py26_test_support as support

import unittest
from test import test_support


class MmapTests(unittest.TestCase):

    def setUp(self):
        # Create a file for the tests
        fp = open(support.TESTFN, 'w+b')
        fp.write(b'\x00' * 1024)
        fp.close()

    def tearDown(self):
        if support.TESTFN in mmap.maps:
            mmap.maps[support.TESTFN].close()
        support.unlink(support.TESTFN)

    def test_basic(self):
        self.assertEqual(mmap.mmap(-1, 1024), None,
                         "Can't open anonymous mmap")

        m = mmap.mmap(0, 1024)
        self.assertE
