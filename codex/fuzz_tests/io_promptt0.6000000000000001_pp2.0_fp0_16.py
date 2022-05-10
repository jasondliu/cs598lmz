import io
# Test io.RawIOBase
class Subclass(io.RawIOBase):
    def fileno(self):
        return 42
    def isatty(self):
        return True
    def read(self, n=-1):
        return "abcde"
    def readinto(self, b):
        b[:5] = 'abcde'
        return 5
    def write(self, b):
        return len(b)
    def seek(self, offset, whence=io.SEEK_SET):
        return 0
    def tell(self):
        return 0
    def truncate(self, size=None):
        return 0

class TestRawIOBase(unittest.TestCase):
    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'))
        self.assertTrue(hasattr(io.RawIOBase, 'name'))

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().fileno)

    def test_isatty(self):

