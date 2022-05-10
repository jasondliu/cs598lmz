import io
# Test io.RawIOBase class.

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

@unittest.skipUnless(hasattr(os, 'dup'), 'os.dup required for this test.')
class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.tearDown()
        fp = open(TESTFN, 'w')
        fp.write('a' * 100000)
        fp.close()
        self.fp = open(TESTFN, 'rb')

    def tearDown(self):
        unlink(TESTFN)

    def test_read(self):
        buf = self.fp.read(100)
        self.assertEqual(len(buf), 100)
        self.assertEqual(buf, b'a'*100)

    def test_seek(self):
        buf = self.fp.read(100)
        self.fp.seek(-50, 1)
        newbuf = self.fp.read(
