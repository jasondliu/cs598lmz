import io
# Test io.RawIOBase
# Test io.RawIOBase.readinto
# Test io.RawIOBase.readinto1
class TestRawIOBase(unittest.TestCase):
    def setUp(self):
        self.r = io.RawIOBase()
        self.b = bytearray(10)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.r.readinto, self.b)

    def test_readinto1(self):
        self.assertRaises(io.UnsupportedOperation, self.r.readinto1, self.b)

# Test io.BufferedIOBase
# Test io.BufferedIOBase.readinto
# Test io.BufferedIOBase.readinto1
class TestBufferedIOBase(unittest.TestCase):
    def setUp(self):
        self.r = io.BufferedIOBase()
        self.b = bytearray(10)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.r.read
