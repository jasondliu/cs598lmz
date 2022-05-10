import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

# ctypes.Structure is a subclass of ctypes.CField
assert issubclass(ctypes.Structure, ctypes.CField)
assert isinstance(S.x, ctypes.CField)
assert isinstance(S.x, ctypes.Structure)

# But ctypes.Structure is not a ctypes.CField
assert not isinstance(C, ctypes.CField)
assert not isinstance(C, ctypes.Structure)
assert not isinstance(C.x, ctypes.CField)
assert not isinstance(C.x, ctypes.Structure)
