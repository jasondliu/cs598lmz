import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function pointer
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# a function pointer as function argument
restype = ctypes.c_int
argtypes = (prototype, ctypes.c_int)

f = prototype((1,))

lib.pass_func_ptr(f, 2)

# a function pointer as return value
restype = prototype
lib.return_func_ptr.restype = restype

f = lib.return_func_ptr()
f(3)

# a function pointer as function attribute
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class X(ctypes.Structure):
    _fields_ = [("funcptr", prototype)]

f = prototype((1,))
x = X()
x.funcptr = f
x.funcptr(4)

# a function pointer as
