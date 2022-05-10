import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        p = POINT(1,2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.x.__class__, ctypes.c_int)
        self.assertEqual(p.y.__class__, ctypes.c_int)

        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_int)]
        s = S(1,2,3,4)
        self.assertEqual(s.a, 1)
        self.assertEqual(s.b, 2)

