import ctypes
# Test ctypes.CField

class CFieldTestCase(unittest.TestCase):
    def test_field_sizeof(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int))

    def test_field_offsetof(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        self.assertEqual(ctypes.addressof(X.x), ctypes.addressof(X))

    def test_field_byref(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        x = X()
        x.x = 42
        self.assertEqual(ctypes.byref(x.x).contents.value, 42)

    def test_field_setattr(self):
        class X(ctypes.Structure):
            _
