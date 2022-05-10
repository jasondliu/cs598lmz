import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int),
                        ('y', ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [('upperleft', POINT),
                        ('lowerright', POINT)]

        class RECT2(ctypes.Structure):
            _fields_ = [('upperleft', POINT),
                        ('lowerright', POINT),
                        ('center', POINT.in_dll(ctypes.CDLL(None), "center"))]

        r = RECT()
        r.upperleft.x = 0
        r.upperleft.y = 1
        r.lowerright.x = 2
        r.lowerright.y = 3
        self.assertEqual(r.upperleft.x, 0)
        self.assertEqual(r.upperleft.y, 1)
        self.assertEqual(r.lowerright.x, 2
