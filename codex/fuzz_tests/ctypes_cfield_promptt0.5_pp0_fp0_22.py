import ctypes
# Test ctypes.CField
class TestCField:
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long)]
        assert X._fields_ == [("x", ctypes.c_long)]
        assert X().x == 0
        X.x = 1
        assert X().x == 1

    def test_pointer(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.POINTER(ctypes.c_long))]
        assert X._fields_ == [("x", ctypes.POINTER(ctypes.c_long))]
        x = X()
        assert x.x == ctypes.POINTER(ctypes.c_long)()
        x.x = 1
        assert x.x == ctypes.POINTER(ctypes.c_long)(1)
        x.x = None
        assert x.x == ctypes.POINTER(ctypes.c_long)()

    def test_struct(self):
        class Y(ctypes.
