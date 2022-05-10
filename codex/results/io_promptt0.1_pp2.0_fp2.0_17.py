import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Read at various positions to test seeking behavior.
        rawio = _io.BytesIO(b"abc")
        self.assertEqual(rawio.read(1), b"a")
        self.assertEqual(rawio.read(1), b"b")
        self.assertEqual(rawio.read(1), b"c")
        self.assertEqual(rawio.read(1), b"")
        rawio.seek(0, 0)
        self.assertEqual(rawio.read(2), b"ab")
        self.assertEqual(rawio.read(1), b"c")
        self.assertEqual(rawio.read(1), b"")
        rawio.seek(0, 0)
        self.assertEqual(rawio.read(3), b"abc")
        self.assertEqual(raw
