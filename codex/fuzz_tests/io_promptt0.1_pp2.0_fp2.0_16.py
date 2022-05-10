import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Test RawIOBase implementation
        rawio = _io.RawIOBase()
        self.assertRaises(OSError, rawio.fileno)
        self.assertRaises(OSError, rawio.isatty)
        self.assertRaises(OSError, rawio.read)
        self.assertRaises(OSError, rawio.readinto, bytearray())
        self.assertRaises(OSError, rawio.readline)
        self.assertRaises(OSError, rawio.readlines)
        self.assertRaises(OSError, rawio.write, b"")
        self.assertRaises(OSError, rawio.seek, 0)
        self.assertRaises(OSError, rawio.tell)
        self.assertRaises(OSError, rawio.truncate)
        self.assertRaises(OS
