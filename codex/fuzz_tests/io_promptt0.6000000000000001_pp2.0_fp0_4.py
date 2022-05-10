import io
# Test io.RawIOBase methods
class RawIOTest(unittest.TestCase):

    def test_read(self):
        self.assertRaises(TypeError, io.RawIOBase().read)
        self.assertRaises(TypeError, io.RawIOBase().read, 10, 20)
        self.assertRaises(TypeError, io.RawIOBase().read, '')
        self.assertRaises(TypeError, io.RawIOBase().read, buffer(b''))
        self.assertRaises(TypeError, io.RawIOBase().read, bytearray(b''))

    def test_readall(self):
        self.assertRaises(TypeError, io.RawIOBase().readall)

    def test_readinto(self):
        self.assertRaises(TypeError, io.RawIOBase().readinto)
        self.assertRaises(TypeError, io.RawIOBase().readinto, '')
        self.assertRaises(TypeError, io.RawIOBase().readinto, buffer(b''))
        self.assertRaises(TypeError
