import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test___init__(self):
        a = ctypes.c_char()
        ctypes.CField(ctypes.Field('a', ctypes.c_char), ctypes.POINTER(a))

        b = ctypes.c_int()
        self.assertRaises(TypeError, ctypes.CField, ctypes.Field('b', ctypes.c_int), ctypes.POINTER(b))

        c = ctypes.c_int()
        self.assertRaises(TypeError, ctypes.CField, ctypes.Field('c', ctypes.c_int), ctypes.c_int)

if __name__ == '__main__':
    unittest.main()
