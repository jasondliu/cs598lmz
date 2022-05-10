import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_double)]
        self.assertEqual(X.x.offset, 0)
        self.assertEqual(X.x.size, 8)
        self.assertEqual(X.x.bitsize, None)
        self.assertEqual(X.x.index, 0)
        self.assertEqual(X.x.pack, 1)
        self.assertEqual(X.x.alignment, 8)
        self.assertEqual(X.x.type, ctypes.c_double)
        self.assertEqual(X.x.name, "x")
        #
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_double, 3)]
        self.assertEqual(X.x.offset, 0)
        self.assertEqual(X.x.size, 24)
        self
