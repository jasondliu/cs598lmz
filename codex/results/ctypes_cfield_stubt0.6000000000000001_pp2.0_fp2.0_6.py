import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

# This should raise a TypeError, not a segfault:
try:
    C()
except TypeError:
    pass
else:
    raise Exception("did not raise TypeError")
