import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        self.assertRaises(TypeError, io.RawIOBase().readinto)
        self.assertRaises(TypeError, io.RawIOBase().readinto, b'')
        self.assertRaises(TypeError, io.RawIOBase().readinto, bytearray(b''))
        self.assertRaises(TypeError, io.RawIOBase().readinto, memoryview(b''))
        self.assertRaises(TypeError, io.RawIOBase().readinto, array('b'))
        self.assertRaises(TypeError, io.RawIOBase().readinto, array('B'))
        self.assertRaises(TypeError, io.RawIOBase().readinto, array('h'))
        self.assertRaises(TypeError, io.RawIOBase().readinto, array('H'))
        self.assertRaises(TypeError, io.RawIOBase().readinto, array('i'))
        self.assertRaises(Type
