import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().read()
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().read(1)
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().read(-1)
    def test_readall(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readall()
    def test_readinto(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readinto(bytearray())
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readinto(bytearray(1))
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readinto(bytearray(-1))
    def test_readinto_buffer(
