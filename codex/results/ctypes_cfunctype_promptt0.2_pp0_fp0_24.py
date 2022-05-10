import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer as argument

# prototype: int (int)
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with", arg)
    return arg + 1

CALLBACKFUNC = CALLBACK(callback)

# prototype: int (int (*)(int), int)
lib.callit.restype = ctypes.c_int
lib.callit.argtypes = (CALLBACK, ctypes.c_int)

print(lib.callit(CALLBACKFUNC, 2))

# call a function with a function pointer as return value

# prototype: int (*)(int)
lib.getit.restype = CALLBACK
lib.getit.argtypes = (ctypes.c_int,)

CALLBACKFUNC = lib.getit(3)
print(CALLBACKFUNC(4
