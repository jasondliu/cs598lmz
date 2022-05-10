import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        pt = POINT(1, 2)
        self.assertEqual(pt.x, 1)
        self.assertEqual(pt.y, 2)
        self.assertEqual(pt[0], 1)
        self.assertEqual(pt[1], 2)
        self.assertEqual(pt[:], (1, 2))
        self.assertEqual(pt[0:], (1, 2))
        self.assertEqual(pt[:2], (1, 2))
        self.assertEqual(pt[0:2], (1, 2))
        self.assertEqual(pt[0:1], (1,))
        self.assertEqual(pt[0:0], ())
        self.assertEqual(pt[0:0:1], ())
        self
