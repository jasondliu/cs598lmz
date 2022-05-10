import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.CField)]
        self.assertEqual(X._fields_, [('a', ctypes.CField)])
        self.assertEqual(X._pack_, 1)
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.CField))
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.CField))
        x = X()
        x.a = 1
        self.assertEqual(x.a, 1)
        x.a = 0
        self.assertEqual(x.a, 0)

    def test_CField_in_union(self):
        class X(ctypes.Union):
            _fields_ = [('a', ctypes.CField)]
        self.assertEqual(X
