import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldPtr = type(ctypes.byref(S.x))

class PyCFuncPtr(ctypes.PyCFuncPtr):
    def _flags_func(self):
        return lambda *args, **kwargs: ctypes.c_void_p()

def test():
    o1 = S()
    o2 = S()
    o1.x = 1
    o2.x = 2
    (p1, p2) = (ctypes.byref(o1.x), ctypes.byref(o2.x))
    assert p1(ctypes.c_int) == 1
    assert p2(ctypes.c_int) == 2
    assert p1(ctypes.c_int(3)) == 3
    assert p2(ctypes.c_int(4)) == 4
    assert p1(ctypes.c_c
