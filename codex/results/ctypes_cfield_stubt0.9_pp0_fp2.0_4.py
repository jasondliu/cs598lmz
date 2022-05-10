import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

try:
    class D(S):
        _fields_ = [('y', ctypes.c_int)]
except TypeError:
    print("SKIP")
    raise SystemExit

print(S.subtypes)
print(D.subtypes)
print(ctypes.c_int.subtypes)
