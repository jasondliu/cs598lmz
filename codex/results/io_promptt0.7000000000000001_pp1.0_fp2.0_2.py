import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().read()

    def test_readinto(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readinto(b'')

    def test_write(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().write(b'')

    def test_fileno(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().fileno()

    def test_isatty(self):
        self.assertIs(io.RawIOBase().isatty(), False)

    def test_seek(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().seek(0, 0)

    def test_tell(self):
        with self.assertRaises(io.UnsupportedOperation):
            io
