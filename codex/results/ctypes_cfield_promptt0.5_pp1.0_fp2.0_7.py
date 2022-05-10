import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class Y(X):
    _fields_ = [("c", ctypes.c_int), ("d", ctypes.c_int)]

class Z(Y):
    _fields_ = [("e", ctypes.c_int), ("f", ctypes.c_int)]

print(ctypes.sizeof(X))
print(ctypes.sizeof(Y))
print(ctypes.sizeof(Z))

## 8
## 16
## 24

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class B(A):
    _fields_ = [("e", ctypes.c_int),
                ("f", ctypes.c_int),
                ("g", ctypes
