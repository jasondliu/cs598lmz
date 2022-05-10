import ctypes
# Test ctypes.CField
class TestCField:
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
            _anonymous_ = ["a"]
        assert X.a.offset == 0
        assert X.b.offset == ctypes.sizeof(ctypes.c_int)

    def test_CField_with_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int, 3),
                        ("d", ctypes.c_int, 29),
                        ("e", ctypes.c_int, 0)]
            _anonymous_ = ["a", "b", "c", "d", "e"]
        assert X.a.offset == 0
        assert X.b.offset == ctypes.sizeof(ctypes.c_int)
        assert X.c.offset
