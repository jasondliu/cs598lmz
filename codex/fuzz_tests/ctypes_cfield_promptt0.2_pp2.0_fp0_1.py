import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))

    def test_CField_in_union(self):
        class X(ctypes.Union):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 0)

# Test ctypes.Structure
class TestStructure(unittest.TestCase):
    def test_Structure(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b",
