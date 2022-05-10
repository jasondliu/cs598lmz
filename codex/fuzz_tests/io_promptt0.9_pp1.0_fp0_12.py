import io
# Test io.RawIOBase which we subclass to implement BufferedIOBase.

import sys
import time
import unittest

from test import support
from test.support import memoryview_leaks


class RawIOBaseTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, "read"))
        self.assertTrue(hasattr(io.RawIOBase, "write"))
        self.assertTrue(hasattr(io.RawIOBase, "fileno"))
        self.assertTrue(hasattr(io.RawIOBase, "isatty"))
        self.assertTrue(hasattr(io.RawIOBase, "close"))
        self.assertTrue(hasattr(io.RawIOBase, "seek"))
        self.assertTrue(hasattr(io.RawIOBase, "tell"))
        self.assertTrue(hasattr(io.RawIOBase, "truncate"))
        self.assertTrue(hasattr(io.RawIOBase, "flush"))
        self.assertTrue(hasattr(io.RawIOBase
