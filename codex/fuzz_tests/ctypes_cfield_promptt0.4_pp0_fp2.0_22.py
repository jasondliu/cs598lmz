import ctypes
# Test ctypes.CField.
import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

x = X()
x.a = 10
x.b = 20

y = Y()
y.x = x

print y.x.a, y.x.b

print X.a
print X.b
print Y.x
print Y.x.a
print Y.x.b

# Test ctypes.CField.
import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

x = X()
x.a = 10
x.b = 20

y = Y()
y.x = x

print y.x.
