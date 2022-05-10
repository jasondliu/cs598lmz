import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read, 0)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto, b'')

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readall)

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().seek)
        self.assertRaises
