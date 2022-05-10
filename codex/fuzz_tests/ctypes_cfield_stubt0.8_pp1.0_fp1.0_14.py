import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

try:
    object.__bases__ = (ctypes.c_int,)
except TypeError:
    print('SKIP')
    raise SystemExit

try:
    S.x.__bases__ = (ctypes.c_int,)
except TypeError:
    print('SKIP')
    raise SystemExit

print(S.x.__bases__) # this does not raise, but does not change S.x's base classes either
