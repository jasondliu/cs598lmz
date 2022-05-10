import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def f(a, b=S.x):
    pass

f(1)
f(1, 2)
f(1, S.x)

def f(a, b=S.x.value):
    pass

f(1)
f(1, 2)
f(1, S.x.value)
</code>

