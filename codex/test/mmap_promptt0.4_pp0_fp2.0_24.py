import mmap
# Test mmap.mmap.write_byte
#
# This test is for mmap.mmap.write_byte()

import os
import unittest
import mmap

from test import test_support

FILENAME = test_support.TESTFN

class MmapTests(unittest.TestCase):

    def setUp(self):
        fp = open(FILENAME, 'w+')
        fp.write('\0' * 1024)
        fp.close()

    def tearDown(self):
        os.unlink(FILENAME)

    def test_write_byte(self):
        fp = open(FILENAME, 'r+')
        m = mmap.mmap(fp.fileno(), 1024)
        m.write_byte('\x00')
        m.write_byte('\xff')
        m.seek(0)
        self.assertEqual(m.read(1), '\x00')
        self.assertEqual(m.read(1), '\xff')
        m.close()
