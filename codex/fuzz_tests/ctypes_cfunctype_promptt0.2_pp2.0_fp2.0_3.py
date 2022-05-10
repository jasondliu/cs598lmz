import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x):
    return x + 1

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
print f(1)

# Test ctypes.POINTER

import ctypes

class POINTER(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return '<POINTER %r>' % self.x

class Test(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.POINTER(ctypes.c_int))]

t = Test()
t.a = 1
t.b = POINTER(2)
print t.a, t.b

# Test ctypes.c_void_p

import ctypes

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_void_p)]
