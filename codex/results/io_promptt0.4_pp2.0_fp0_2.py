import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_constructor(self):
        # Test RawIOBase.__init__
        self.assertRaises(TypeError, io.RawIOBase)
        self.assertRaises(TypeError, io.RawIOBase, 10)
        self.assertRaises(TypeError, io.RawIOBase, "")
        self.assertRaises(TypeError, io.RawIOBase, "", "")

    def test_read(self):
        # Test RawIOBase.read
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read, 10)

    def test_readinto(self):
        # Test RawIOBase.readinto
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytear
