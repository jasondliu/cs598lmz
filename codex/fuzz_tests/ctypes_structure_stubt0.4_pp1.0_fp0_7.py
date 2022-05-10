import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char

class T(ctypes.Structure):
    _fields_ = [("y", ctypes.c_char)]

class U(ctypes.Structure):
    _fields_ = [("z", ctypes.c_char)]

class V(T, U):
    pass

class W(U, T):
    pass

class X(T, S):
    pass

class Y(S, T):
    pass

class Z(S, V):
    pass

class A(V, S):
    pass

class B(S, W):
    pass

class C(W, S):
    pass

for klass in [S, T, U, V, W, X, Y, Z, A, B, C]:
    print klass.__name__, klass._fields_

print S.__mro__
print T.__mro__
print U.__mro__
print V.__mro__
print W.__mro__
print X.__mro__
print Y.
