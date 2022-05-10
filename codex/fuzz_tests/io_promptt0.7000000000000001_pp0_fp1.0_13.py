import io
# Test io.RawIOBase
import sys
import unittest

from test import support


class RawIOTestCase(unittest.TestCase):
    def test_rawio(self):
        # This is just a smoke test; the base class isn't meant to be instantiated
        r = io.RawIOBase()
        self.assertIs(r.read(0), bytes())
        self.assertRaises(io.UnsupportedOperation, r.read)
        self.assertEqual(r.write(b'abc'), 3)
        self.assertRaises(io.UnsupportedOperation, r.seek, 0)
        self.assertRaises(io.UnsupportedOperation, r.tell)
        self.assertRaises(io.UnsupportedOperation, r.truncate)
        self.assertRaises(io.UnsupportedOperation, r.fileno)

        # Test context manager
        with self.assertRaises(TypeError) as cm:
            with r:
                pass
        self.assertEqual(str(cm.exception),
                         "raw stream cannot be used in a context manager")
