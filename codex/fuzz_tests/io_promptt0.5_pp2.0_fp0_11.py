import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # testing read()
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.read)
        # self.assertRaises(TypeError, r.read, 10)
        self.assertRaises(TypeError, r.read, 'x')
        self.assertRaises(TypeError, r.read, None)
        self.assertRaises(TypeError, r.read, 10, 20)
        # self.assertRaises(TypeError, r.readinto, 'x')
        # self.assertRaises(TypeError, r.readinto, bytearray(b'x'))
        # self.assertRaises(TypeError, r.readinto, None)
        # self.assertRaises(TypeError, r.readinto, b'x', None)
        # self.assertRaises(TypeError, r.readinto, bytearray(b'x'), None)
        # self.assertRaises(
