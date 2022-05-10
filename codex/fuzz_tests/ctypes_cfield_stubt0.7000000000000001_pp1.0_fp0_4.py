import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# this is the actual call to the C function that defines the type
# at runtime
ctypes.CField.__new__ = ctypes.CField.__new_
