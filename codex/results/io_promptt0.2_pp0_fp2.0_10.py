import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# The io module is not available on all platforms
try:
    io
except NameError:
    raise unittest.SkipTest("io module not available")

class RawIOBaseTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'),
                        "'mode' attribute not found")
        self.assertTrue(hasattr(io.RawIOBase, 'name'),
                        "'name' attribute not found")

    def test_abc(self):
        self.assertTrue(io.RawIOBase.__abstractmethods__)
        self.assertTrue(io.RawIOBase.readinto.__isabstractmethod__)
        self.assertTrue(io.RawIOBase.read.__isabstractmethod__)
        self.assertTrue(io.RawIOBase.write.__isabstractmethod__)
        self.assertTrue
