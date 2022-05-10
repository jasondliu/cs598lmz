import io
# Test io.RawIOBase, io.BufferedIOBase, io.TextIOBase

import unittest

class BasicsTest(unittest.TestCase):

    def test_IOBase(self):
        f = io.IOBase()
        self.assertRaises(UnsupportedOperation, f.fileno)
        self.assertRaises(UnsupportedOperation, f.isatty)
        self.assertRaises(UnsupportedOperation, f.tell)
        self.assertRaises(UnsupportedOperation, f.seek, 0)
        self.assertRaises(UnsupportedOperation, f.truncate, 0)
        self.assertRaises(UnsupportedOperation, f.read)
        self.assertRaises(UnsupportedOperation, f.readinto, bytearray())
        self.assertRaises(UnsupportedOperation, f.readline)
        self.assertRaises(UnsupportedOperation, f.readlines, ())
        self.assertRaises(UnsupportedOperation, f.write, "")
        self.assertRaises(UnsupportedOperation, f.writelines, ())

