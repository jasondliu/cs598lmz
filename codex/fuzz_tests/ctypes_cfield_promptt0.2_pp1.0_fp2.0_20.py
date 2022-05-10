import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual(POINT.y.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(POINT), 2 * ctypes.sizeof(ctypes.c_int))

    def test_CField_with_alignment(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual(POINT.y.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(
