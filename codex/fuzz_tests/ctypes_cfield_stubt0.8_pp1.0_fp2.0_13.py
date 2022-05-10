import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    _fields_ = [('f', ctypes.CField)]

assert type(C.f) is ctypes.CField
assert C.f.__doc__ == "CField(c_int) -> c_int"

# ctypes.PyCFuncPtr is a subclass of ctypes.CFunctionType
assert issubclass(ctypes.PyCFuncPtr, ctypes.CFunctionType)
