import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'))
        self.assertTrue(hasattr(io.RawIOBase, 'name'))
        self.assertTrue(hasattr(io.RawIOBase, 'close'))
        self.assertTrue(hasattr(io.RawIOBase, 'closed'))
        self.assertTrue(hasattr(io.RawIOBase, 'fileno'))
        self.assertTrue(hasattr(io.RawIOBase, 'isatty'))
        self.assertTrue(hasattr(io.RawIOBase, 'read'))
        self.assertTrue(hasattr(io.RawIOBase, 'readable'))
        self.assertTrue(hasattr(io.RawIOBase, 'readinto'))
        self.assertTrue(hasattr(io.RawIOBase, 'readline'))
        self.assertTrue
