import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Testing read()
        self.assertRaises(TypeError, io.RawIOBase().read)
        self.assertRaises(TypeError, io.RawIOBase().read, 'x')
        self.assertRaises(TypeError, io.RawIOBase().read, 10, 'x')

    def test_readinto(self):
        # Testing readinto()
        self.assertRaises(TypeError, io.RawIOBase().readinto)
        self.assertRaises(TypeError, io.RawIOBase().readinto, 'x')
        self.assertRaises(TypeError, io.RawIOBase().readinto, bytearray(10), 'x')

    def test_write(self):
        # Testing write()
        self.assertRaises(TypeError, io.RawIOBase().write)
        self.assertRaises(TypeError, io.RawIOBase().write, '')
        self.assertRaises(TypeError, io.RawIOBase
