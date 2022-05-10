import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)


class CFunc(ctypes._FuncPtr):
    pass
ctypes.CFunc = CFunc

def func(*args, **kw):
    return CFunc()

ctypes.CFuncPtr = type(CFunc)

ctypes.ArgType = type(ctypes.c_int)

# look in the ctypes._pointer_type_cache
ctypes._Pointer = ctypes.POINTER(ctypes.c_int)

def CFixedArray(cls):
    return cls

ctypes.CFixedArray = type(ctypes.c_short * 32)
ctypes.CArray = ctypes.CFixedArray in ctypes._pointer_type_cache
