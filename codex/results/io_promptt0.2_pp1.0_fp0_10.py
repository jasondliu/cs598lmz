import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Test read()
        self.assertRaises(TypeError, io.RawIOBase().read)
        self.assertRaises(TypeError, io.RawIOBase().read, 10, 20)
        self.assertRaises(TypeError, io.RawIOBase().read, 'x')
        self.assertRaises(TypeError, io.RawIOBase().read, buffer='x')
        self.assertRaises(TypeError, io.RawIOBase().read, memoryview('x'))
        self.assertRaises(TypeError, io.RawIOBase().read, bytearray('x'))
        self.assertRaises(TypeError, io.RawIOBase().read, memoryview(bytearray('x')))
        self.assertRaises(TypeError, io.RawIOBase().read, array.array('B', b'x'))
        self.assertRaises(TypeError, io.RawIOBase().read, memoryview(array.array('B
