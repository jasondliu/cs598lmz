import ctypes
# Test ctypes.CField, ctypes.CStruct, and ctypes.Structure

# This is a bug on cygwin32, if the parameter is a tuple: ArgumentError: argument 1: <type 'exceptions.TypeError'>: wrong type
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char * 10),
                ("c", ctypes.c_char * 10)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char * 10),
                ("c", ctypes.c_char * 10)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char * 10),
                ("c", ctypes.c_char * 10)]

class W(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z", Z)]

