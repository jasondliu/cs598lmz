import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_simple(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        p = POINT(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(ctypes.sizeof(p), ctypes.sizeof(ctypes.c_int) * 2)
        self.assertEqual(ctypes.addressof(p.x), ctypes.addressof(p))
        self.assertEqual(ctypes.addressof(p.y), ctypes.addressof(p) + ctypes.sizeof(ctypes.c_int))
        self.assertEqual(p.x, ctypes.cast(ctypes.addressof(p), ctypes.POINTER(ctypes.c_int))[0])
        self.assertEqual(p.
