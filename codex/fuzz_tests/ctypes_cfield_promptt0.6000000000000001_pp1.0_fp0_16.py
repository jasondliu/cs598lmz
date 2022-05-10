import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int)]

class Z(X, Y):
    _fields_ = [("c", ctypes.c_int)]

if __name__ == "__main__":
    import test.test_support
    test.test_support.run_unittest(__name__)
