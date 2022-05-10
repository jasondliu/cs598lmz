import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x + 1

def func_with_exception(x):
    raise ValueError

def func_with_fatal(x):
    ctypes.string_at(0)

for argtypes in [ctypes.c_int, ctypes.c_float, ctypes.c_double]:
    for restype in [ctypes.c_int, ctypes.c_float, ctypes.c_double]:
        f = ctypes.CFUNCTYPE(restype, argtypes)(func)
