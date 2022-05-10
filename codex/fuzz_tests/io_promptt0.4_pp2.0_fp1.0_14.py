import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
import weakref

from test import support


class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(_io.RawIOBase, 'mode'))
        self.assertTrue(hasattr(_io.RawIOBase, 'name'))
        self.assertTrue(hasattr(_io.RawIOBase, 'close'))
        self.assertTrue(hasattr(_io.RawIOBase, 'closed'))
        self.assertTrue(hasattr(_io.RawIOBase, 'fileno'))
        self.assertTrue(hasattr(_io.RawIOBase, 'flush'))
        self.assertTrue(hasattr(_io.RawIOBase, 'isatty'))
        self.assertTrue(hasattr(_io.RawIOBase, 'read'))
        self.assertTrue(hasattr(_io.RawIOBase, 'readable'))
        self.assertTrue(hasattr(_io.RawIOBase, 'read
