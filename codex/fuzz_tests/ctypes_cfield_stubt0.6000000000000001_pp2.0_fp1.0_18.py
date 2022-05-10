import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyCFuncPtr(ctypes.CFuncPtr):
    _flags_ = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(S), ctypes.c_int)

    def __call__(self, *args):
        return self._flags_(self)(*args)

f = MyCFuncPtr(lambda s, x: s.contents.x + x)

s = S(42)
print f(s, 3)
