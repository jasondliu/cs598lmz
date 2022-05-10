import io
# Test io.RawIOBase

import sys
import unittest
from test import test_support

from io import RawIOBase

class TestRawIO(RawIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def fileno(self):
        return -1
    def close(self):
        pass

class TestRawIOBase(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(RawIOBase, 'mode'))
        self.assertTrue(hasattr(RawIOBase, 'name'))
        self.assertTrue(hasattr(RawIOBase, 'close'))
        self.assertTrue(hasattr(RawIOBase, 'closed'))
        self.assertTrue(hasattr(RawIOBase, 'fileno'))
        self.assertTrue(hasattr(RawIOBase, 'flush'))
        self.assertTrue(hasattr(RawIOBase, 'isatty'))
        self.assertTrue(has
