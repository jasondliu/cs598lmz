import ctypes
# Test ctypes.CField
class TestCField:
    def test_CField_basic(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char_p),
                        ("c", ctypes.c_int)]
        x = X()
        assert x.a == 0
        assert x.b == None
        assert x.c == 0
        x.a = 42
        x.b = "hello"
        x.c = -1
        assert x.a == 42
        assert x.b == "hello"
        assert x.c == -1

    def test_CField_array(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int * 3)]
        x = X()
        assert x.a[0] == 0
        assert x.a[1] == 0
        assert x.a[2] == 0
        x.a[0] = 42
        x.a[1] = 43
       
