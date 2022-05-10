import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        # Test that ctypes.CField() works
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))

        # Test that ctypes.CField() works with nested structures
        class Y(ctypes.Structure):
            _fields_ = [("c", ctypes.c_int),
                        ("x", X)]
        self.assertEqual(Y.c.offset, 0)
        self.assertEqual(Y.x.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(Y.x.a.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(Y.x.b.offset,
