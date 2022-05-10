import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.readinto, b'')
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray())

    def test_readall(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.readall)

    def test_read1(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.read1, 0)

    def test_read(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.read)
        self.assertRaises(io.UnsupportedOperation, f.read, 0)

    def test_readline(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.readline
