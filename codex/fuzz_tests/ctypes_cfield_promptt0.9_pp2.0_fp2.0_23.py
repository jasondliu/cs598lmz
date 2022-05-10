import ctypes
# Test ctypes.CField
class DoublePtr(ctypes.c_double):
    _type_ = "d"
    _subtype_ = ctypes.POINTER

class Structure(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double),
                ("f", ctypes.c_double),
                ("next", DoublePtr)]

# Test POINTER(ctypes.c_long)
class Structure2(ctypes.Structure):
    _fields_ = [("long_ptr", ctypes.POINTER(ctypes.c_long)),
                ("double_ptr", ctypes.POINTER(ctypes.c_double))]

class DivisionByZero_error(Exception): pass

def cfunc(lib, name):
    "Simplify calling ctypes functions with old-style C names"
    return getattr(lib, "_"+name)

# load the shared library
mydll = cdll.LoadLibrary("dlltest")

for name in ("one_
