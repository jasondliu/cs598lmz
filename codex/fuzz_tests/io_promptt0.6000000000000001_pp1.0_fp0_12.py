import io
# Test io.RawIOBase, io.BufferedIOBase and io.TextIOBase

# Test io.BaseRawIO

class RawIOBaseTests(unittest.TestCase):

    def test_readinto(self):
        b = io.BytesIO(b"hello world")
        self.assertRaises(io.UnsupportedOperation, b.raw.readinto, bytearray(5))

    def test_detach(self):
        b = io.BytesIO(b"hello world")
        self.assertRaises(io.UnsupportedOperation, b.raw.detach)

    def test_seekable(self):
        b = io.BytesIO(b"hello world")
        self.assertTrue(b.raw.seekable())
        b = io.BytesIO(b"hello world")
        b.seek(5)
        self.assertTrue(b.raw.seekable())
        b = io.BytesIO(b"hello world")
        b.read(5)
        self.assertTrue(b.raw.seekable())

    def test_readable(self):

