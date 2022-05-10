import ctypes
# Test ctypes.CFUNCTYPE(func, arg1, arg2, ...)

def functype(arg):
    "My CFUNCTYPE calling function"
    if arg == 42:
        return 12
    raise ValueError

CFUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f = CFUNCTYPE(functype)

if f(42) != 12:
    raise RuntimeError

try:
    f(43)
except ValueError:
    pass
