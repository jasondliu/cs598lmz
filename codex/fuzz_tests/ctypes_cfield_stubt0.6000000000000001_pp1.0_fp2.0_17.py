import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFuncPtr(ctypes.Structure):
    _fields_ = [('p', ctypes.CFUNCTYPE(None))]

# this works
CFuncPtr.p.__set__(None, lambda: None)

# this doesn't
CFuncPtr.p.__set__(None, ctypes.c_int)

# this does, but we shouldn't have to do it this way
CFuncPtr.p.__set__(None, ctypes.cast(ctypes.c_int, ctypes.CFUNCTYPE(None)))
