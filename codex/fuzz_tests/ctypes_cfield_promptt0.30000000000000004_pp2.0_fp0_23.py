import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual(POINT.y.offset, 4)
        self.assertEqual(POINT.x.size, 4)
        self.assertEqual(POINT.y.size, 4)
        self.assertEqual(POINT.x.index, 0)
        self.assertEqual(POINT.y.index, 1)
        self.assertEqual(POINT.x.type, ctypes.c_int)
        self.assertEqual(POINT.y.type, ctypes.c_int)
        self.assertEqual(POINT.x.name, "x")
        self.assertEqual(POINT.y.name, "y")
        self.assertEqual(POINT
