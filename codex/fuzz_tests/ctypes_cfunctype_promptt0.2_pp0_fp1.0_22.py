import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

restype = ctypes.c_int
argtypes = (ctypes.c_int, ctypes.c_int)

# call a function
func = lib.add
func.restype = restype
func.argtypes = argtypes

res = func(1, 2)
if res != 3:
    raise RuntimeError("function call failed")

# call a function pointer
func = ctypes.c_void_p.in_dll(lib, "add_ptr").value
func.restype = restype
func.argtypes = argtypes

res = func(1, 2)
if res != 3:
    raise RuntimeError("function pointer call failed")

# call a function pointer in a structure
class S(ctypes.Structure):
    _fields_ = [("func", ctypes.CFUNCTYPE(restype, *argtypes))]

s = S.in_dll(lib, "s")
res = s.func(1, 2)
