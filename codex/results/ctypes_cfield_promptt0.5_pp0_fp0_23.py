import ctypes
# Test ctypes.CField.from_param

class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

cf = ctypes.CField.from_param

assert cf(C.x) is C.x
assert cf(C) is C
assert cf(C(1)) is C(1)

try:
    cf(1)
except TypeError:
    pass
else:
    raise Exception

try:
    cf(None)
except TypeError:
    pass
else:
    raise Exception
