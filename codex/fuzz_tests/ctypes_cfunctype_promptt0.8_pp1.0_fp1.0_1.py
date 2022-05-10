import ctypes
# Test ctypes.CFUNCTYPE()
proto = ctypes.CFUNCTYPE
# Test bytearray()
class TestBytearray(unittest.TestCase):
    def test_ctor(self):
        self.assertRaises(TypeError, bytearray)
        self.assertRaises(TypeError, bytearray, 'abc')
        self.assertRaises(TypeError, bytearray, 'abc', 'latin1')
        self.assertRaises(TypeError, bytearray, memoryview(b'abc'))
        self.assertEqual(bytearray(b'abc'), bytearray(b'abc'))
        self.assertEqual(bytearray(b'abc'), bytearray(b'abc', 'ascii'))
        self.assertEqual(bytearray(b'abc'), bytearray(memoryview(b'abc')))
        self.assertEqual(bytearray(b'abc'), bytearray(array.array('B', b'abc')))
        self.assert
