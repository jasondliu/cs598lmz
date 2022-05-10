import io
# Test io.RawIOBase
class _TestRawIOBase(BaseTestIOBase):
    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.io.read)
    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto,
                          self.buffer)
    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readall)
    def test_readable(self):
        self.assertFalse(self.io.readable())
    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto,
                          self.buffer)
    def test_readline(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readline)
    def test_readlines(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readlines)
    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation
