import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref
import sys

# Base class for testing a RawIOBase implementation.
# The class to test is given as the constructor parameter.
# The test does not assume that read() and readinto() are implemented.
class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = self.build_io()
        self.f.__init__(self.support.get_data_files())
        self.f.seek(0)

    def tearDown(self):
        self.f.close()
        self.f = None

    def test_read(self):
        self.assertEqual(self.f.read(0), b'')
        self.assertEqual(self.f.read(5), self.support.sample[:5])
        self.assertEqual(self.f.read(7), self.support.sample[5:12])
        self.assertEqual(self.f.read(5), self.support.sample[12:17])
