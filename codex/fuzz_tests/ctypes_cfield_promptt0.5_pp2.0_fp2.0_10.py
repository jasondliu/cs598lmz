import ctypes
# Test ctypes.CField.from_address on a non-structure type.
import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_char * 100)]

if __name__ == "__main__":
    Xref = ctypes.POINTER(X)
    x = X()
    xref = Xref.from_address(ctypes.addressof(x))
    xref.contents.a = 1
    xref.contents.b = 2
    xref.contents.c[0] = '\x03'
    xref.contents.c[1] = '\x04'
    xref.contents.c[2] = '\x05'
    _ctypes_test.expect_eq(x.a, 1)
    _ctypes_test.expect_eq(x.b, 2)
    _ctypes_test.expect_eq(x.c[
