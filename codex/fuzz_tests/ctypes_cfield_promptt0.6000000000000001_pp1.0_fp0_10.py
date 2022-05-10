import ctypes
# Test ctypes.CField.from_address().
# This test is for the case where we have an array of structs with
# several fields, and we want to use the array to access the structs.
import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("s", ctypes.c_char * 4),
                ("x", X * 3)]

class Z(ctypes.Structure):
    _fields_ = [("p", ctypes.POINTER(X)),
                ("n", ctypes.c_int)]

lib.make_structs.restype = Y
lib.get_y.restype = ctypes.POINTER(Y)

def test():
    y = lib.make_structs()
    y_p = y.x
    assert isinstance(y_p, ctypes.Array
