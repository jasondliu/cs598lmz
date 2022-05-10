import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("b", C)]

class E(ctypes.Structure):
    _fields_ = [("c", ctypes.POINTER(C))]

class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_int),
                ("c", ctypes.c_char)]

# Test ctypes.CFuncPtr
def func(x):
    return x

CFUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
func_ptr = CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

# Test ctypes.CArray
class CArray(ctypes.Structure):
    _fields_ = [('numbers', ctypes.c_int * 5)]

# Test ctypes
