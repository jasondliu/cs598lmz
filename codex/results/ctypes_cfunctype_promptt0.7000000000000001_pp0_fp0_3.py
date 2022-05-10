import ctypes
# Test ctypes.CFUNCTYPE()

# This should create a CFUNCTYPE object with the specified argtypes and
# restype.

def callback(arg):
    return arg

CbType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
assert isinstance(CbType, type)

cb = CbType(callback)
assert isinstance(cb, CbType)

assert cb(42) == 42
