import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# The following test is a bit of a lie, since it doesn't actually
# check that the fields are in the correct order, but it's better
# than nothing.

class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [('b', ctypes.c_int)]

class C(A, B):
    _fields_ = [('c', ctypes.c_int)]

class D(C, B):
    _fields_ = [('d', ctypes.c_int)]

class E(D, A):
    _fields_ = [('e', ctypes.c_int)]

class F(E, B):
    _fields_ = [('f', ctypes.c_int)]

class G(F, A):
    _fields_ = [('g', ctypes.c_int)]

class H(G, B):
    _fields_ = []

class I(H, A):
    _fields_
