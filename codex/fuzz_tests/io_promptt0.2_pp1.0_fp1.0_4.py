import io
# Test io.RawIOBase

import io
import unittest
import weakref
from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # This is a mixin test for RawIOBase.  It doesn't test anything
        # specific to the raw I/O implementation.
        rawio = support.MockRawIO()
        self.assertEqual(rawio.mode, 'rb')
        self.assertEqual(rawio.name, 'foo')
        self.assertEqual(rawio.isatty(), False)
        self.assertEqual(rawio.readable(), True)
        self.assertEqual(rawio.writable(), False)
        self.assertEqual(rawio.seekable(), False)
        self.assertRaises(io.UnsupportedOperation, rawio.tell)
        self.assertRaises(io.UnsupportedOperation, rawio.seek, 0)
        self.assertRaises(io.UnsupportedOperation, rawio.truncate)
        self.assertRaises(io.Un
