import io
# Test io.RawIOBase
class TestRawIO(unittest.TestCase):
    def test_read(self):
        # Test RawIO.read()
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.read, 10)

    def test_readinto(self):
        # Test RawIO.readinto()
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, bytearray())
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, memoryview(bytearray(10)))

    def test_write(self):
        # Test RawIO.write()
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.write, b"")
        rawio = io.RawIOBase()
        self
