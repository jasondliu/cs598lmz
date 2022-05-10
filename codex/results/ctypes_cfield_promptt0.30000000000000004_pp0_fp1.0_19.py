import ctypes
# Test ctypes.CField

class CFieldTestCase(unittest.TestCase):

    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.a.pack, 1)
        self.assertEqual(X.a.ctype, ctypes.c_int)
        self.assertEqual(X.a.type, ctypes.c_int)
        self.assertEqual(X.a.name, "a")

    def test_simple_2(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
       
