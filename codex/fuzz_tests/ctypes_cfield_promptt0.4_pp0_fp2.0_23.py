import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield_simple(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        p = POINT(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_cfield_array(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int * 3)]

        p = POINT((1, 2, 3))
        self.assertEqual(p.x[0], 1)
        self.assertEqual(p.x[1], 2)
        self.assertEqual(p.x[2], 3)

    def test_cfield_nested(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y",
