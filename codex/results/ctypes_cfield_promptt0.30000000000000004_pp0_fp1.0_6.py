import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_basic(self):
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        s = S()
        self.assertEqual(ctypes.sizeof(s), ctypes.sizeof(ctypes.c_int)*2)
        self.assertEqual(s.a, 0)
        self.assertEqual(s.b, 0)
        s.a = 42
        self.assertEqual(s.a, 42)
        self.assertEqual(s.b, 0)
        s.b = -42
        self.assertEqual(s.a, 42)
        self.assertEqual(s.b, -42)
        s.a = 0x12345678
        self.assertEqual(s.a, 0x12345678)
        self.assertEqual(s.b, -42)
        s.b = 0x87654321

