import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int)*2)
        self.assertEqual(ctypes.sizeof(X.a), ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(X.b), ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.alignment(X), ctypes.alignment(ctypes.c_int))
        self.assertEqual(ctypes.alignment(X.a), ctypes.alignment(ctypes.c_int))
        self.assertEqual(ctypes.alignment(X.b), ctypes.alignment(ctypes.c_int))
        self.assertEqual(ct
