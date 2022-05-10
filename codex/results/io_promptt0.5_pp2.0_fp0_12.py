import io
# Test io.RawIOBase

# This test checks that RawIOBase methods exist, but makes
# no attempt to check that they work.

import io
import os
import sys
import unittest

from test import support
from test.support import TESTFN

class TestRawIOBase(unittest.TestCase):

    def setUp(self):
        support.unlink(TESTFN)

    def tearDown(self):
        support.unlink(TESTFN)

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'),
                        "RawIOBase is missing the 'mode' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'name'),
                        "RawIOBase is missing the 'name' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'close'),
                        "RawIOBase is missing the 'close' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'closed'),
                        "RawIOBase is missing the 'closed' attribute")
        self.assertTrue
