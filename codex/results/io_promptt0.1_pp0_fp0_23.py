import io
# Test io.RawIOBase

import unittest
from test import support
from io import BytesIO, BufferedReader, BufferedWriter, BufferedRWPair, BufferedRandom
from io import DEFAULT_BUFFER_SIZE

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Read nothing
        b = io.BytesIO()
        self.assertEqual(b.read(), b"")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(1), b"")
        self.assertEqual(b.read(-1), b"")
        self.assertEqual(b.read(None), b"")

        # Read exact
        b = io.BytesIO(b"abc")
        self.assertEqual(b.read(), b"abc")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(1), b"")
        self.assertEqual(b.read(-1), b"")
       
