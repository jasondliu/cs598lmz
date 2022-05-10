import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)
    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
            bytearray())
    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readall)
    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')
    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().seek, 0)
    def test_tell(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().tell)
    def test_truncate(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().truncate)
    def test
