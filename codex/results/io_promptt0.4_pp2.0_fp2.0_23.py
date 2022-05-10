import io
# Test io.RawIOBase

import _io

class RawIOTest(unittest.TestCase):

    def test_read(self):
        f = _io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.read)
        self.assertRaises(io.UnsupportedOperation, f.read, 10)
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray(b" "))
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray(b" "), 10)
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray(b" "), 10)
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray(b" "), 10)
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray(b" "), 10)

    def test_readall(self):
        f = _io.RawIOBase()
        self.assertRaises(
