import io
# Test io.RawIOBase

import _io

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Should not accept negative arguments
        self.assertRaises(ValueError, _io.RawIOBase().read, -1)

    def test_readinto(self):
        # Should not accept negative arguments
        self.assertRaises(ValueError, _io.RawIOBase().readinto, bytearray(1))
        self.assertRaises(ValueError, _io.RawIOBase().readinto, bytearray(1), -1)
        self.assertRaises(ValueError, _io.RawIOBase().readinto, bytearray(1), 0, -1)

    def test_write(self):
        # Should not accept negative arguments
        self.assertRaises(ValueError, _io.RawIOBase().write, b"")
        self.assertRaises(ValueError, _io.RawIOBase().write, b"", -1)
        self.assertRaises(ValueError, _io.RawIOBase().write
