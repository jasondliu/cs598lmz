import ctypes
# Test ctypes.CField
cField = ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_offset(self):
        # This test just makes sure that the offset is being set properly
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 4)

    def test_subclass(self):
        # This tests that the offset is correct even when there is a subclass
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        class Y(X):
            _fields_ = [("b", ctypes.c_int)]
        self.assertEqual(Y.a.offset, 0)
        self.assertEqual(Y.b.offset, 4)

    def test_subclass_override(self):
        # This tests that the offset is correct when there is a
