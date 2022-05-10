import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual(POINT.y.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.x.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.y.size, ctypes.sizeof(ctypes.c_int))

    def test_CField_in_Union(self):
        class POINT(ctypes.Union):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual(POINT.y.offset, 0)
        self
