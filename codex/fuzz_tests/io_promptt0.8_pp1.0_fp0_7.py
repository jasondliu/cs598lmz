import io
# Test io.RawIOBase

class RawIOTest(unittest.TestCase):
    def setUp(self):
        self.b = io.BytesIO()
        self.r = io.RawIOBase()
        self.r.writable = lambda: True
        self.r.write = lambda b: self.b.write(b)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.r.read)
        self.assertRaises(io.UnsupportedOperation, self.r.read, 1)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.r.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, self.r.readinto,
                          array.array('b', [0]))

    def test_read1(self):
        self.assertRaises(io.UnsupportedOperation, self.r.read1)
        self.assertRaises(io.UnsupportedOperation, self.r.read1, 1)

    def
