import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class T(ctypes.Structure):
    _fields_ = [("p", ctypes.POINTER(S))]

t = T()

t.p = ctypes.pointer(S(1))
t.p.contents.x = 2

print t.p.contents.x
</code>

