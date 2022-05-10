import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read, 1)
    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
            bytearray())
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
            bytearray(1))
    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')
    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().seek, 0)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().seek, 0, 0)
    def test_tell(self):
        self.assertRaises(io.Unsupported
