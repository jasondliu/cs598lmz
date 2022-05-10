import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Make sure we can instantiate all the classes

class TestRawIOBase(unittest.TestCase):
    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'),
                        "RawIOBase is missing the 'mode' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'name'),
                        "RawIOBase is missing the 'name' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'close'),
                        "RawIOBase is missing the 'close' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'closed'),
                        "RawIOBase is missing the 'closed' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'fileno'),
                        "RawIOBase is missing the 'fileno' attribute")
        self.assertTrue(hasattr(io.RawIOBase, '
