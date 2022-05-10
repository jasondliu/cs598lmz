import ctypes
# Test ctypes.CField in a C structure that has a sub-structure.
# The following structure is defined in an external library.
class S(ctypes.Structure):
    _fields_ = [("d", ctypes.c_int), ("s", ctypes.c_char_p)]

# The following structure is defined in Python code.
class T(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int), ("s", ctypes.CFiel
