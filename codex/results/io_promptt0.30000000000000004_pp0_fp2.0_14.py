import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'),
                         "RawIOBase instance has no attribute 'mode'")
        self.assertTrue(hasattr(io.RawIOBase, 'name'),
                         "RawIOBase instance has no attribute 'name'")

    def test_abc(self):
        self.assertTrue(io.RawIOBase.close)
        self.assertTrue(io.RawIOBase.closed)
        self.assertTrue(io.RawIOBase.fileno)
        self.assertTrue(io.RawIOBase.isatty)
        self.assertTrue(io.RawIOBase.read)
        self.assertTrue(io.RawIOBase.readinto)
        self.assertTrue(io.RawIOBase.readline)
        self.assertTrue(io.RawIOBase.seek)
        self.assertTrue(io.RawIO
