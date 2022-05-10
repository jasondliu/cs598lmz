import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', S)]

c = C()
c.x = S()
c.x.x = 42
print c.x.x
</code>

