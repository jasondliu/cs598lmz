import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char * 4)]
        self.assertEqual(ctypes.sizeof(X), 8)
        self.assertEqual(X._fields_, [("a", ctypes.c_int), ("b", ctypes.c_char * 4)])

# Test ctypes.Structure
class TestStructure(unittest.TestCase):
    def test_basic(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char * 4)]
        x = X()
        self.assertEqual(ctypes.sizeof(x), 8)
        self.assertEqual(x._fields_, [("a", ctypes.c_int), ("b", ctypes.c_char * 4)])
       
