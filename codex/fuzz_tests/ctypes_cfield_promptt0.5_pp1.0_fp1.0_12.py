import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_single(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual(POINT.y.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.x.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.y.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.x.index, 0)
        self.assertEqual(POINT.y.index, 1)

    def test_array(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int * 3),
                        ("y", ctypes.c_int * 4)]
        self
