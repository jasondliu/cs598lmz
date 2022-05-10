import io
# Test io.RawIOBase class methods
import io

class RawIOTest(unittest.TestCase):

    def test_read(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.read)

    def test_readinto(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.readinto, b'')

    def test_write(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.write, b'')

    def test_seek(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.seek, 0)

    def test_tell(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.tell)

    def test_truncate(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.truncate
