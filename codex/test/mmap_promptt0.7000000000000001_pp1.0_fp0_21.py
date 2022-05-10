import mmap
# Test mmap.mmap.write()
#

import unittest
import sys
from test import test_support

class MmapWriteTest(unittest.TestCase):
    def setUp(self):
        size = 1024
        self.f = open(test_support.TESTFN, 'w+b')
        self.f.write('\0' * size)
        self.f.flush()
        self.m = mmap.mmap(self.f.fileno(), size)

    def tearDown(self):
        self.m.close()
        self.f.close()
        test_support.unlink(test_support.TESTFN)

    def test_write_string(self):
        self.m.write('abc')
        self.assertEqual(self.m[:3], 'abc')
        self.assertEqual(self.f.tell(), 0)

    def test_write_unicode(self):
        self.m.write(unicode('abc'))
        self.assertEqual(self.m[:3], 'abc')
       
