import ctypes
# Test ctypes.CFUNCTYPE
def C_FUNC(restype, *argtypes):
    return ctypes.CFUNCTYPE(restype, *argtypes)
