import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

ctypes.CFunc = type(ctypes.cast)

def f(x):
    return x

ctypes.CFuncPtr = type(ctypes.CFUNCTYPE(ctypes.c_int)(f))

class C2(ctypes.Structure):
    _fields_ = [('x', ctypes.CFuncPtr)]

ctypes.CFuncPtrPtr = type(ctypes.pointer(ctypes.CFuncPtr))

class C3(ctypes.Structure):
    _fields_ = [('x', ctypes.CFuncPtrPtr)]

ctypes.CArray = type(ctypes.c_int * 1)

class C4(ctypes.Structure):
    _fields_ = [('x', ctypes.CArray)]

ctypes.CArrayPtr = type(ctypes.pointer(ctypes.c_int * 1))

class C5(ctypes.Structure):
    _fields_ =
