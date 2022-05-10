import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def raise_error():
	raise RuntimeError("You're a piece of shit")

ctypes.raise_error = raise_error

class CField(ctypes.CPointer):
    _type_ = ctypes.CFuncPtr

ctypes.CFuncPtr = type(raise_error)

ctypes.LP_c_int = ctypes.POINTER(ctypes.c_int)

class LP_S(ctypes.POINTER(S)):
    pass

ctypes.LP_S = LP_S

class LP_CFuncPtr(ctypes.POINTER(ctypes.CFuncPtr)):
    pass

ctypes.LP_CFuncPtr = LP_CFuncPtr

def sizeof(tp):
    return ctypes.sizeof(tp)

ctypes.sizeof = sizeof

def byref(obj):
    if not isinstance(obj, ctypes._SimpleCData):
        obj = ctypes.c_void_p(obj)
    return ctypes.byref(obj)

if hasattr(ctypes,
