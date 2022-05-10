import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_int)]
            _anonymous_ = ["b"]

        # test that the ctypes.CField is accessible
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))

        # test that the ctypes.CField is writable
        X.b = ctypes.c_int
        self.assertEqual(X._fields_[1], ("b", ctypes.c_int))

        # test that the ctypes.CField is readable
        self.assertEqual(X.b, ctypes.c_int)

        # test that the ctypes.CField is deletable
        del X.b
        self.assertEqual(X._fields_, [("a
