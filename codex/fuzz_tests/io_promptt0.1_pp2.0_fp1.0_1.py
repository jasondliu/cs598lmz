import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# Issue #7995: if sys.stdout is a StringIO, io.TextIOWrapper will crash
# when trying to call its write() method.
class TestCrash(unittest.TestCase):
    def setUp(self):
        self.saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_main(self):
        # This test is supposed to run *without* crashing.
        io.TextIOWrapper(io.BytesIO())

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Read nothing
        b = io.BytesIO()
        self.assertEqual(b.read(), b"")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.
