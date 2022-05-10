import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        f = io.RawIOBase()
        self.assertRaises(NotImplementedError, f.readinto, b'')
        self.assertRaises(NotImplementedError, f.write, b'')
        self.assertRaises(io.UnsupportedOperation, f.fileno)
        self.assertRaises(io.UnsupportedOperation, f.seekable)
        self.assertRaises(io.UnsupportedOperation, f.readable)
        self.assertRaises(io.UnsupportedOperation, f.writable)


class BytesIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        f = io.BytesIO()
        self.assertRaises(NotImplementedError, f.readinto, b'')
        self.assertRaises(NotImplementedError, f.write, b'')
        self.assertRaises(io.UnsupportedOperation, f.fileno)
        self.assertRa
