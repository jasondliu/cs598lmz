import io
# Test io.RawIOBase

import io
import os
import unittest
import weakref
from test import support
from test.support import TESTFN, unlink

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_read(self):
        b = self.f.read(3)
        self.assertEqual(len(b), 0)
        self.assertRaises(TypeError, self.f.read)

    def test_readinto(self):
        b = bytearray(3)
        n = self.f.readinto(b)
        self.assertEqual(n, 0)
        self.assertEqual(len(b), 3)
        self.assertRaises(TypeError, self.f.readinto)

    def test_write(self):
        self.assertRaises(TypeError, self
