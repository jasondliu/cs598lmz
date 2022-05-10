import io
# Test io.RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        # Test readinto()
        b = bytearray(b"abc")
        self.assertRaises(TypeError, io.RawIOBase.readinto, b)

    def test_readall(self):
        # Test readall()
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readall)

    def test_read(self):
        # Test read()
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_read1(self):
        # Test read1()
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read1)

    def test_write(self):
        # Test write()
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b"")

    def test_fileno(self):
        # Test fileno()
        self.assertRaises(io.UnsupportedOperation,
