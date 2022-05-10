import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        pt = POINT(10, 20)
        self.assertEqual(pt.x, 10)
        self.assertEqual(pt.y, 20)

    def test_cfield_repr(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        pt = POINT(10, 20)
        self.assertEqual(repr(pt), "POINT(x=10, y=20)")

    def test_cfield_repr_with_name(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int, "X"),
                        ("y", ctypes.c_int, "
