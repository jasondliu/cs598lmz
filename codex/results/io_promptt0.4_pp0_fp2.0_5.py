import io
# Test io.RawIOBase

import unittest

from test import support
from test.support import TESTFN, run_unittest

import io

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Test RawIOBase using a StringIO object
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, b"")
        self.assertRaises(io.UnsupportedOperation, rawio.readline)
        self.assertRaises(io.UnsupportedOperation, rawio.write, b"")
        self.assertRaises(io.UnsupportedOperation, rawio.seek, 0)
        self.assertRaises(io.UnsupportedOperation, rawio.tell)
        self.assertRaises(io.UnsupportedOperation, rawio.truncate)
        self.assertRaises(io.UnsupportedOperation, rawio.fileno)
        self.assertRaises(io.Unsupported
