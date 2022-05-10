import ctypes
# Test ctypes.CField

class TestCField:
    def test_simple(self):
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        s = S()
        assert s.a == 0

    def test_unnamed(self):
        class S(ctypes.Structure):
            _fields_ = [("", ctypes.c_int)]
        s = S()
        assert s._0 == 0

    def test_unnamed_2(self):
        class S(ctypes.Structure):
            _fields_ = [("", ctypes.c_int), ("", ctypes.c_int)]
        s = S()
        assert s._0 == 0
        assert s._1 == 0

    def test_unnamed_3(self):
        class S(ctypes.Structure):
            _fields_ = [("", ctypes.c_int), ("", ctypes.c_int), ("", ctypes.c_int)]
        s = S()
        assert s._0 == 0
        assert s._1
