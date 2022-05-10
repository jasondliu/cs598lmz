import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(POINT), ctypes.sizeof(ctypes.c_int)*2)
        self.assertEqual(ctypes.alignment(POINT), ctypes.alignment(ctypes.c_int))
        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual(POINT.y.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.x.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.y.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.x.index, 0)
        self.assertEqual(POINT.y
