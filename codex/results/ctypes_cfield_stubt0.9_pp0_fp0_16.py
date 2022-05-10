import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
cint = ctypes.c_int
assert isinstance(cint(42), int)

try:
    ctypes.CField.__add__(1)
except TypeError as exn:
    print(exn)
else:
    print("TypeError not raised")
