import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

C._fields_[0] = ('y', ctypes.c_int)

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

try:
    D._fields_[0] = (1, ctypes.c_int)
except TypeError:
    pass
else:
    print("did not raise TypeError")

try:
    D._fields_ = []
except TypeError:
    pass
else:
    print("did not raise TypeError")

try:
    D._fields_ = [('x', ctypes.c_int, 1)]
except TypeError:
    pass
else:
    print("did not raise TypeError")

try:
    D._fields_ = [('x', ctypes.c_int), ('x', ctypes.c_int)]
except ValueError:
    pass
else:
    print("did not raise ValueError")

try
