import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(S))]

s = S()
s.x = 42
c = C()
c.p = ctypes.pointer(s)
print(c.p.contents.x)
</code>

