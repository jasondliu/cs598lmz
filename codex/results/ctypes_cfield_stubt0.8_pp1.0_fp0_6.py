import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    x: ctypes.c_int

C.x = type(S.x)

def f(x: ctypes.c_int):
    pass

f(type(S.x))

class D:
    def f(self, x: ctypes.c_int):
        pass

D().f(type(S.x))
