import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_c_field(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        pt = POINT(10, 20)
        self.assertEqual(pt.x, 10)
        self.assertEqual(pt.y, 20)
        self.assertEqual(pt[0], 10)
        self.assertEqual(pt[1], 20)
        self.assertRaises(TypeError, pt.__setitem__, 0, "hello")
        self.assertRaises(TypeError, pt.__setitem__, 1, "hello")
        pt[0] = 30
        pt[1] = 40
        self.assertEqual(pt.x, 30)
        self.assertEqual(pt.y, 40)
        self.assertEqual(pt[0], 30)
        self.assertEqual(pt[1], 40)
        self.assertE
