import ctypes
# Test ctypes.CFUNCTYPE and ctypes.c_int.
class TestCFUNCTYPO(unittest.TestCase):

    def test_c_int(self):
        self.assertEqual(ctypes.sizeof(ctypes.c_int), ctypes.sizeof(ctypes.c_long))
        self.assertEqual(ctypes.sizeof(ctypes.c_int), ctypes.sizeof(ctypes.c_void_p))
        self.assertEqual(ctypes.sizeof(ctypes.c_int), ctypes.sizeof(ctypes.py_object))

    def test_c_float(self):
        self.assertEqual(ctypes.sizeof(ctypes.c_float), ctypes.sizeof(ctypes.c_double))

    def test_c_double(self):
        self.assertEqual(ctypes.sizeof(ctypes.c_double), ctypes.sizeof(ctypes.c_longdouble))

    def test_c_char(self):
        self.assertEqual(ctypes.sizeof(
