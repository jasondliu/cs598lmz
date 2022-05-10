import io
# Test io.RawIOBase class

import unittest
from io import BytesIO

from test import test_support

class RawIOTest(unittest.TestCase):
    def test_rawio(self):
        self.assertRaises(TypeError, io.RawIOBase)
        self.assertRaises(TypeError, io.FileIO, "foo", "w")
        self.assertRaises(TypeError, io.FileIO, "foo", "rw")
        self.assertRaises(TypeError, io.FileIO, "foo", "rw", 0)
        self.assertRaises(TypeError, io.FileIO, "foo", "rw", 0, True)
        self.assertRaises(TypeError, io.FileIO, "foo", "rw", 0, True, "utf8")

        # Test read()
        f = io.BytesIO(b"abc")
        self.assertEqual(f.read(), b"abc")
        self.assertEqual(f.read(), b"")

        f = io.BytesIO(b"abc")
        self.
