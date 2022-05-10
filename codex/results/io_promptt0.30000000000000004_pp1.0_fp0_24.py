import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)
    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
            bytearray())
    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readall)
    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')
    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().fileno)
    def test_readable(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readable)
    def test_writable(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().writable)
    def test_seek
