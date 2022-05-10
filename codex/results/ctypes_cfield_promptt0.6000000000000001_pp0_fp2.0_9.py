import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [
                ("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)
                ]
            _anonymous_ = ("b",)
        self.assertEqual(X._fields_, [("a", ctypes.c_int), ("c", ctypes.c_int)])
        x = X()
        self.assertEqual(x.a, 0)
        self.assertEqual(x.b, 0)
        self.assertEqual(x.c, 0)
        x.a = 42
        x.b = 13
        x.c = 666
        self.assertEqual(x.a, 42)
        self.assertEqual(x.b, 13)
        self.assertEqual(x.c, 666)
        self.assertEqual(ctypes.sizeof(x), ctypes
