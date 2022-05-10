import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        x = X()
        self.assertEqual(x.a, 0)
        self.assertEqual(x.b, 0)
        x.a = 42
        self.assertEqual(x.a, 42)
        self.assertEqual(x.b, 0)
        x.b = -1
        self.assertEqual(x.a, 42)
        self.assertEqual(x.b, -1)
        del x.a
        self.assertEqual(x.a, 0)
        self.assertEqual(x.b, -1)
        del x.b
        self.assertEqual(x.a, 0)
        self.assertEqual(x.b, 0)
        self.assertRaises(AttributeError, getattr, x, "c
