import ctypes
# Test ctypes.CField
class TestCField:
    def test_basic(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        assert X.a.offset == 0
        assert X.b.offset == 4
        assert X.a.size == 4
        assert X.b.size == 4
        assert X.a.index == 0
        assert X.b.index == 1

    def test_unnamed(self):
        class X(ctypes.Structure):
            _fields_ = [("", ctypes.c_int),
                        ("", ctypes.c_int)]
        assert X._fields_ == [("", ctypes.c_int),
                              ("", ctypes.c_int)]
        assert X.a.offset == 0
        assert X.b.offset == 4
        assert X.a.size == 4
        assert X.b.size == 4
        assert X.a.index == 0
        assert X.b.index == 1

    def
