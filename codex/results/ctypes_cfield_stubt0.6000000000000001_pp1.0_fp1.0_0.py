import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    x = ctypes.c_int()

class D(object):
    x = ctypes.c_int(0)

class E(object):
    x = ctypes.c_int(42)

class F(object):
    x = ctypes.c_int.in_dll(ctypes.CDLL(''), 'x')

print C().x
print D().x
print E().x
print F().x

# The same for functions

ctypes.CFuncPtr = type(ctypes.CFUNCTYPE(ctypes.c_int)())

class X(object):
    x = ctypes.CFUNCTYPE(ctypes.c_int)()

print X().x

# and arrays

ctypes.CArray = type(ctypes.c_int * 3)

class Y(object):
    x = ctypes.c_int * 3

print Y().x

class Z(object):
    x = ctypes.c_int * 3
    def __init__
