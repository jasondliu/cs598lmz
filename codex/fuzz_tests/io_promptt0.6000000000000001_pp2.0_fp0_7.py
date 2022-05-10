import io
# Test io.RawIOBase
# io.RawIOBase.readinto()
# io.RawIOBase.seek()
# io.RawIOBase.tell()
# io.RawIOBase.truncate()

class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        # Test readinto()
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().readinto)
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().readinto, bytearray())

    def test_seek(self):
        # Test seek()
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().seek)
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().seek, 0)
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().seek, 0, 0)

    def test_tell(self):
        # Test tell()
        self.assertRaises(io.Unsupported
