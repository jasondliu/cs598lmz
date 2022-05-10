import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        s = S()
        self.assertEqual(s.a, 0)
        self.assertEqual(s.b, 0)
        s.a = 42
        self.assertEqual(s.a, 42)

    def test_cfield_in_union(self):
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        class U(ctypes.Union):
            _fields_ = [("s", S),
                        ("c", ctypes.c_int)]
        u = U()
        self.assertEqual(u.s.a, 0)
        self.assertEqual(u.s.b, 0)
        u.s.a = 42
        self
