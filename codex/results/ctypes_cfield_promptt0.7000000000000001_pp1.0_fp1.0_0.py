import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("char", ctypes.c_char),
                ("short", ctypes.c_short),
                ("int", ctypes.c_int),
                ("long", ctypes.c_long),
                ("longlong", ctypes.c_longlong),
                ("float", ctypes.c_float),
                ("double", ctypes.c_double),
                ("char_p", ctypes.c_char_p)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("p", ctypes.POINTER(X)),
                ("s", ctypes.c_short)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char * 5),
                ("b", ctypes.c_char * 5),
                ("c", ctypes.c_char * 5)]

def test_CField():
    value = Y.x.in_dll(ctypes.c_long(), "value")

    assert
