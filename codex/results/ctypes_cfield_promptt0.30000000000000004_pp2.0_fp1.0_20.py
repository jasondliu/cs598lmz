import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        p = POINT(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p[0], 1)
        self.assertEqual(p[1], 2)
        self.assertEqual(p[:], (1, 2))
        self.assertEqual(p[::-1], (2, 1))
        self.assertEqual(p[::1], (1, 2))
        self.assertEqual(p[::2], (1,))
        self.assertEqual(p[::-2], (2,))
        self.assertEqual(p[::-3], (2,))
        self.assertEqual(p[::-4], ())
        self
