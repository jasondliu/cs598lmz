import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    _fields_ = [('x', ctypes.c_int)]

assert type(C.x) is ctypes.CField

try:
    class D(object):
        __slots__ = ['x']
        x = ctypes.c_int
except TypeError:
    pass
else:
    print('No TypeError raised')

class E(object):
    __slots__ = ['x']

E.x = ctypes.c_int

class F(object):
    __slots__ = ['x']
    def __init__(self):
        self.x = ctypes.c_int
F().x = 1

# Test ctypes.Structure.from_address()

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class B(A):
    _fields_ = [('y', ctypes.c_int)]

a = A()
b = B.from_address(ctypes.addressof(a))
assert
