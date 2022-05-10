import ctypes
# Test ctypes.CField.sizeof

class TestSizeof(unittest.TestCase):

    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X.a.sizeof, ctypes.sizeof(ctypes.c_int))

    def test_pointer(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.POINTER(ctypes.c_int))]
        self.assertEqual(X.a.sizeof, ctypes.sizeof(ctypes.POINTER(ctypes.c_int)))

    def test_array(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int * 2)]
        self.assertEqual(X.a.sizeof, ctypes.sizeof(ctypes.c_int) * 2)

    def test_nested(self):
        class X(ctypes.Structure):
            _fields_
