import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.read)

    def test_readinto(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.readinto, b"")

    def test_write(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.write, b"")

    def test_fileno(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.fileno)

    def test_isatty(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.isatty)

    def test_seek(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.seek, 0)

    def
