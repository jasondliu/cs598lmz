import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        pt = POINT(1, 2)
        self.assertEqual(pt.x, 1)
        self.assertEqual(pt.y, 2)
        pt.x = 3
        pt.y = 4
        self.assertEqual(pt.x, 3)
        self.assertEqual(pt.y, 4)

    def test_cfield_get_set(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        pt = POINT()
        pt.x = 1
        pt.y = 2
        self.assertEqual(pt.x, 1)
        self.assertEqual(pt.y, 2)

    def test_cfield
