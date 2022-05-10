import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class B(A):
    _fields_ = [('y', ctypes.c_int)]

class C(A):
    _fields_ = [('z', ctypes.c_int)]

class D(B, C):
    _fields_ = [('w', ctypes.c_int)]


def main():
    # Issue #15901: ctypes.Structure.__setattr__() should not raise an
    # exception if the attribute name is not a valid Python identifier.
    class E(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    e = E()
    e.x = 1
    e.y = 2
    e.z = 3
    e.t = 4
    e.u = 5
    e.v = 6
    e.w = 7
    assert e.x == 1
    assert e.y == 2

