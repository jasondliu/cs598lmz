import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(isinstance(S.x, ctypes.CField))

if sys.version_info >= (3,):
    ctypes.PyCField = type(S.x)
else:
    ctypes.PyCField = type(S.x.value)
print(isinstance(S.x, ctypes.PyCField))

class S1(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]
    def __init__(self):
        pass
    def __str__(self):
        return 'S1()'

class S2(S1):
    _fields_ = S1._fields_ + [('c', ctypes.c_int)]
    _anonymous_ = ['a']
    def __str__(self):
        return 'S2()'

print(S2())

import sys, os
if sys.platform == 'darwin':
    libc = ctypes.CDLL('libc.dylib')
else:
    libc =
