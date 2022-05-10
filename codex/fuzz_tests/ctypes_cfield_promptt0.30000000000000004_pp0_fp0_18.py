import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_offsetof(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.addressof(X.a), ctypes.addressof(X))
        self.assertEqual(ctypes.addressof(X().a), ctypes.addressof(X()))
        self.assertEqual(ctypes.addressof(X.a), ctypes.addressof(X))
        self.assertEqual(ctypes.addressof(X().a), ctypes.addressof(X()))
        self.assertEqual(ctypes.addressof(X.a), ctypes.addressof(X))
        self.assertEqual(ctypes.addressof(X().a), ctypes.addressof(X()))
        self.
