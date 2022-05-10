import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Issue #7995: _RawIOBase methods should raise OSError
        # instead of IOError.
        f = io.RawIOBase()
        self.assertRaises(OSError, f.read)
        self.assertRaises(OSError, f.readinto, bytearray())
        self.assertRaises(OSError, f.readline)
        self.assertRaises(OSError, f.write, b'')
        self.assertRaises(OSError, f.fileno)
        self.assertRaises(OSError, f.seek, 0)
        self.assertRaises(OSError, f.tell)
        self.assertRaises(OSError, f.truncate)
        self.assertRaises(OSError, f.readall)
        self.assertRaises(OSError, f.
