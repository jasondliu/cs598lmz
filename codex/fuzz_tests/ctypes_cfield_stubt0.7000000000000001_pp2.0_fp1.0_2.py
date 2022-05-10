import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

try:
    type(S.x)
except AttributeError:
    print("SKIP")
    raise SystemExit

print(type(S.x))
print(type(S.x) is type(ctypes.c_int))
print(isinstance(S.x, ctypes.CField))
print(isinstance(S.x, ctypes.c_int))
