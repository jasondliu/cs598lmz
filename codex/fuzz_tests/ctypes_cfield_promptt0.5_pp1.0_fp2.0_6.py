import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        self.assertEqual(POINT.x.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.y.offset, 2 * ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.x.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.y.size, ctypes.sizeof(ctypes.c_int))

    def test_cfield_in_union(self):
        class POINT(ctypes.Union):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual
