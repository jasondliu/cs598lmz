import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", X)]

# Y -> X

f = ctypes.CFUNCTYPE(X, Y)(lambda y: y.x)

y = Y(X(1, 2), X(3, 4))
x = f(y)

print(x.a, x.b)

# X -> Y

f = ctypes.CFUNCTYPE(Y, X)(lambda x: Y(x, x))

x = X(1, 2)
y = f(x)

print(y.x.a, y.x.b, y.y.a, y.y.b)

# Y -> Y

f = ctypes.CFUNCTYPE(Y, Y)(lambda y: Y(y.y, y
