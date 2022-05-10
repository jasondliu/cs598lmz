import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('c', ctypes.c_char)]

class B(A):
    _fields_ = A._fields_ + [('s', ctypes.c_short)]

class C(B):
    _fields_ = B._fields_ + [('i', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = C._fields_ + [('f', F)]


# Use a Field instance as a function's return value
def foo():
    return D.f

assert foo() is D.f

def bar(x):
    return x.f

assert bar(D) is D.f

# Use a Field instance as a function's argument
def sqr(x):
    return x.x * x.x

assert sqr(S()) == 0


# set the integer value of an S
s = S()
s.x = 42

