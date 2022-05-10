import ctypes
# Test ctypes.CField

class CFieldTestCase(unittest.TestCase):
    def test_field_sizeof(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_char),
                        ("b", ctypes.c_short),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_long),
                        ("e", ctypes.c_longlong),
                        ("f", ctypes.c_float),
                        ("g", ctypes.c_double),
                        ("h", ctypes.c_longdouble),
                        ("i", ctypes.c_void_p)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_longdouble) + ctypes.sizeof(ctypes.c_void_p))

    def test_field_offsetof(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_char),
                        ("b", ctypes.c_short),
                        ("
