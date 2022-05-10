import io
# Test io.RawIOBase

import _io

class TestRawIOBase(_io.IOBase):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.read)
        self.assertRaises(io.UnsupportedOperation, self.IO.read, 10)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.readinto, bytearray(10))

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.write, b"")
        self.assertRaises(io.UnsupportedOperation, self.IO.write, memoryview(b""))

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.seek)
        self.assertRaises(io.UnsupportedOperation, self.IO.seek, 0)
        self.assertRaises(io.UnsupportedOperation, self.IO.seek, 0, 0)

    def test_tell(self):
        self.assertRa
