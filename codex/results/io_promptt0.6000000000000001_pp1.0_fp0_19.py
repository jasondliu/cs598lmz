import io
# Test io.RawIOBase implementation
import io
import sys
import unittest

import sio

class IOTest(unittest.TestCase):
    def test_rawiobase_attrs(self):
        self.assertEqual(sio.RawIOBase.mode, None)
        self.assertEqual(sio.RawIOBase.name, None)
        self.assertEqual(sio.RawIOBase.closed, False)

    def test_rawiobase_notimplemented(self):
        self.assertRaises(NotImplementedError, sio.RawIOBase().read)
        self.assertRaises(NotImplementedError, sio.RawIOBase().readinto)
        self.assertRaises(NotImplementedError, sio.RawIOBase().readline)
        self.assertRaises(NotImplementedError, sio.RawIOBase().readlines)
        self.assertRaises(NotImplementedError, sio.RawIOBase().write, b"")
        self.assertRaises(NotImplementedError,
