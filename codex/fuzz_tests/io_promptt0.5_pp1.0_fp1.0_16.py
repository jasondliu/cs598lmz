import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        with self.assertRaises(NotImplementedError):
            io.RawIOBase().read()
    def test_write(self):
        with self.assertRaises(NotImplementedError):
            io.RawIOBase().write(b'\0')
    def test_seek(self):
        with self.assertRaises(NotImplementedError):
            io.RawIOBase().seek(0)
    def test_tell(self):
        with self.assertRaises(NotImplementedError):
            io.RawIOBase().tell()
    def test_readinto(self):
        with self.assertRaises(NotImplementedError):
            io.RawIOBase().readinto(bytearray(1))
    def test_readinto_negative_arg(self):
        with self.assertRaises(ValueError):
            io.RawIOBase().readinto(bytearray(-1))
    def test_readall(self):

