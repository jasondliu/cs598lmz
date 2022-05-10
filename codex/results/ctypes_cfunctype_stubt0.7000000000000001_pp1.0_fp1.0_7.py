import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return b"x"

class bytesTest(unittest.TestCase):
    def test_from_parms(self):
        self.assertEqual([b'x', b'y'], list(map(
            bytes, [bytearray(b'x'), bytearray(b'y')])))

    def test_from_iterable(self):
        self.assertEqual(b"xy", bytes(i for i in [b'x', b'y']))

    def test_from_sequence(self):
        self.assertEqual(b"abc", bytes(b'abc'))
        self.assertRaises(TypeError, bytes, [65, 66])
        self.assertRaises(TypeError, bytes, [65, 66])
        self.assertRaises(TypeError, bytes, "xyz")
        self.assertEqual(b'abc', bytes(bytearray(b'abc')))

    def test_from_buffer(self):
        self.assertEqual(b"def", bytes(b"abcdef", 2
