import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x) # No longer a property
ctypes.Structure._fields_ = [('y', ctypes.c_int)]
S._fields_ = [('z', ctypes.c_int)]

class T(ctypes.Structure):
    pass
try:
    T._fields_ = []
except TypeError:
    print("TypeError")

class U(ctypes.Structure):
    _fields_ = [('dummy', ctypes.c_int)]
try:
    U._fields_ = []
except TypeError:
    print("Exception")

class V(Structure):
    _fields_ = [('dummy', ctypes.c_int)]
try:
    V._fields_ = []
except TypeError:
    print("Exception")
