import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('y', ctypes.CField)]

class Y(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

X.y.__set_name__(X, 'y')
Y.y.__set_name__(Y, 'y')
Z.y.__set_name__(Z, 'y')

print(X.y)
print(Y.y)
print(Z.y)

print(X.y == Y.y)
print(X.y == Z.y)
print(Y.y == Z.y)
</code>

