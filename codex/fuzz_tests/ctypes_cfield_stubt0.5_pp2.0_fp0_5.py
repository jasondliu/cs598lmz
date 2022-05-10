import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

c = C(S(42))
print c.x.x
c.x.x = 99
print c.x.x
</code>
The only problem is that the <code>CField</code> constructor is not exposed in the <code>ctypes</code> module, so you have to do this hack.

