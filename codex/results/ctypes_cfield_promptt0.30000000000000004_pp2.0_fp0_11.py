import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]
        self.assertEqual(RECT._fields_,
                         [("ul", POINT), ("lr", POINT)])
        self.assertEqual(RECT._fields_[0][1]._fields_,
                         [("x", ctypes.c_int), ("y", ctypes.c_int)])
        self.assertEqual(RECT._fields_[1][1]._fields_,
                         [("x", ctypes.c_int), ("y", ctypes.c_int)])

    def test_cfield_subclass(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c
