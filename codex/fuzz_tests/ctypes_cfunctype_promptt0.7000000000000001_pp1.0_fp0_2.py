import ctypes
# Test ctypes.CFUNCTYPE
def C_FUNC(restype, *argtypes):
    return ctypes.CFUNCTYPE(restype, *argtypes)
C_FUNC(c_int, c_int)
# Test ctypes.POINTER
def POINTER(obj):
    return ctypes.POINTER(obj)
POINTER(c_int)
# Test ctypes.WINFUNCTYPE
def WIN_FUNC(restype, *argtypes):
    return ctypes.WINFUNCTYPE(restype, *argtypes)
WIN_FUNC(c_int, c_int)
# Test ctypes.Structure
def Structure(name, *args, **kwargs):
    return ctypes.Structure(name, *args, **kwargs)
Structure("Number", [("value", c_int)])
# Test ctypes.Union
def Union(name, *args, **kwargs):
    return ctypes.Union(name, *args, **kwargs)
Union("Number", [("value", c_int)])
# Test ctypes.create_string_buffer
