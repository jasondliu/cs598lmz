import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_sizeof(self):
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int),
                        ('b', ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), 8)

    def test_offsetof(self):
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int),
                        ('b', ctypes.c_int)]
        self.assertEqual(ctypes.addressof(X.b),
                         ctypes.addressof(X.a) + ctypes.sizeof(X.a))

    def test_in_structure(self):
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int),
                        ('b', ctypes.c_int)]
        self.assertEqual(X.b.offset, ctypes.sizeof(X.a))

    def test_
