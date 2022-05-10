import mmap
# Test mmap.mmap.__new__().

import os, re, sys, unittest
import mmap

class MmapTests(unittest.TestCase):
    def setUp(self):
        # Create a file and write a few lines to it
        f = open(support.TESTFN, 'w+')
        f.write('\n' * 16)
        f.write('line1\n')
        f.write('line2\n')
        f.write('line3\n')
        f.close()

    def tearDown(self):
        os.unlink(support.TESTFN)

    def test_constructor(self):
        f = open(support.TESTFN, 'r+')
        m = mmap.mmap(f.fileno(), 16)
        self.assertEqual(m.size(), 16)
        m.close()
        f.close()

        f = open(support.TESTFN, 'r+')
