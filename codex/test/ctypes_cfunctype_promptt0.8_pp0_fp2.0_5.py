import ctypes
# Test ctypes.CFUNCTYPE works as intended
def make_c_callable(func, restype, argtypes):
    return ctypes.CFUNCTYPE(restype, *argtypes)(func)

