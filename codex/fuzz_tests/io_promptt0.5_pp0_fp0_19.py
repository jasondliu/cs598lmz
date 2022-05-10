import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):

    # Return a new RawIOBase implementation.
    # The returned implementation must support the readinto() method.
    def new_io(self, *args):
        raise NotImplementedError

    def test_read(self):
        io = self.new_io(b"ABCDE")
        self.assertEqual(io.read(0), b"")
        self.assertEqual(io.read(1), b"A")
        self.assertEqual(io.read(2), b"BC")
        self.assertEqual(io.read(3), b"DE")
        self.assertEqual(io.read(4), b"")
        self.assertEqual(io.read(5), b"")
        self.assertEqual(io.read(6), b"")
        self.assertEqual(io.read(), b"")
        self.assertEqual(io.read(), b"")

    def test_readinto(self):
        io = self.new_io(
