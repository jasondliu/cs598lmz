import io
# Test io.RawIOBase.readinto() method.

import io
import os
import sys
import tempfile
import unittest

from test import support

class ReadIntoTest(unittest.TestCase):
    def setUp(self):
        self.rawio = io.RawIOBase()
        self.tempdir = tempfile.TemporaryDirectory()
        self.filename = os.path.join(self.tempdir.name, "test.txt")

    def tearDown(self):
        self.tempdir.cleanup()

    def test_readinto_regular_file(self):
        # Issue #17525: readinto() should work with regular files.
        with open(self.filename, "wb") as f:
            f.write(b"abc")
        with open(self.filename, "rb") as f:
            buf = bytearray(1)
            self.assertEqual(f.readinto(buf), 1)
            self.assertEqual(buf, b"a")
            self.assertEqual(f.readinto(buf), 1)
           
