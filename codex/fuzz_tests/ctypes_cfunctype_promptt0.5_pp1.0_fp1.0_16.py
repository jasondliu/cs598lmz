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
        assert f(argtypes(42)) == restype(43)
        f = ctypes.CFUNCTYPE(restype, argtypes)(func_with_exception)
        raises(ValueError, f, argtypes(42))
        f = ctypes.CFUNCTYPE(restype, argtypes)(func_with_fatal)
        raises(ValueError, f, argtypes(42))

# Test ctypes.CFUNCTYPE with a structure pointer argument

class X(ctypes.Structure):

