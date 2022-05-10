import io
# Test io.RawIOBase.readall.

import io
import sys
import unittest

class TestReadall(unittest.TestCase):

    def test_readall(self):
        # Test readall() on a RawIOBase object.
        b = io.BytesIO(b"abc")
        self.assertEqual(b.readall(), b"abc")
        b.close()

        # Test readall() on a BufferedIOBase object.
        b = io.BufferedReader(io.BytesIO(b"abc"))
        self.assertEqual(b.readall(), b"abc")
        b.close()

        # Test readall() on a TextIOBase object.
        # TextIOWrapper doesn't support readall().
        b = io.TextIOWrapper(io.BytesIO(b"abc"), encoding="ascii")
        self.assertRaises(io.UnsupportedOperation, b.readall)
        b.close()

    def test_readall_negative(self):
        # Test readall() on a closed RawIOBase object.

