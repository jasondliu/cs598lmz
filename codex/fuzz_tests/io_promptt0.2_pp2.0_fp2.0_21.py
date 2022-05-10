import io
# Test io.RawIOBase

import _io

class RawIOTest(unittest.TestCase):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().readinto,
                          bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().write,
                          b"")

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().fileno)

    def test_isatty(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().isatty)

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().seek, 0)

    def test_tell(self):
        self.assertRaises(io.
