import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

# The following will raise an exception in python 2.6, but not in 2.7, 3.2
# or 3.3
D()
C()
