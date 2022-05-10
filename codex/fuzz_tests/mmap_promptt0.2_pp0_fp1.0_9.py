import mmap
# Test mmap.mmap()
#
# This test is derived from the mmap module test suite.
#
# Copyright (c) 2001-2004 Python Software Foundation; All Rights Reserved
#
# Author: Guido van Rossum

import os
import unittest
import mmap

from test import test_support

class MmapTests(unittest.TestCase):

    def setUp(self):
        fp = open(test_support.TESTFN, 'w+b')
        fp.write('\0' * 1024)
        fp.close()
        self.map = mmap.mmap(fp.fileno(), 1024)

    def tearDown(self):
        self.map.close()
        os.unlink(test_support.TESTFN)

    def test_find(self):
        self.assertEqual(self.map.find('a'), -1)
        self.assertEqual(self.map.find('a', 1), -1)
        self.map[0] = 'a'
        self.assertEqual(self.map.find('
