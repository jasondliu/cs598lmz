import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(S)

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.POINTER(T))]

class C(object):
    def m(self):
        pass

class U(ctypes.Structure):
    _fields_ = [("x", ctypes.PYFUNCTYPE(None, ctypes.POINTER(U)))]

for T in [S, T, U]:
    C.m.__ctypes_from_outparam__ = lambda self, type: T()
    C.m.restype = T
    x = C()
    x.m()
##
x=ctypes.c_int(3)
assert x.value == 3
assert x.value == ctypes.cast(x, ctypes.POINTER(ctypes.c_int))[0]
##
ctypes.CFUNCTYPE(ctypes.c_int)(lambda: ctypes.c_int(5))()
##
ctypes.CFUNCTYPE(ctypes.c_int,

