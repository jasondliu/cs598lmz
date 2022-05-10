import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(X), 2 * ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.alignment(X), ctypes.alignment(ctypes.c_int))
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.b.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.name, "a")
        self.assertEqual(X.b.name, "b")

