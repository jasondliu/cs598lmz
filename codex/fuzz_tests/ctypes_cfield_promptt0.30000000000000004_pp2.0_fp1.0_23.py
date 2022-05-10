import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_c_field(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual(POINT.y.offset, ctypes.sizeof(ctypes.c_int))

        class RECT(ctypes.Structure):
            _fields_ = [("a", POINT),
                        ("b", POINT)]
        self.assertEqual(RECT.a.offset, 0)
        self.assertEqual(RECT.b.offset, 2 * ctypes.sizeof(ctypes.c_int))

    def test_c_array(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        class RECT(ctypes.Structure):
            _fields
