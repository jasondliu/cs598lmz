import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        pt = POINT(10, 20)
        self.assertEqual(pt.x, 10)
        self.assertEqual(pt.y, 20)
        self.assertEqual(pt[0], 10)
        self.assertEqual(pt[1], 20)
        self.assertEqual(pt[:], [10, 20])
        pt.x = 30
        pt.y = 40
        self.assertEqual(pt.x, 30)
        self.assertEqual(pt.y, 40)
        self.assertEqual(pt[0], 30)
        self.assertEqual(pt[1], 40)
        self.assertEqual(pt[:], [30, 40])
        pt[0] = 50
        pt[1] = 60
        self.assert
