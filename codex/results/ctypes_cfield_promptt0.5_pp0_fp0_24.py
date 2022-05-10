import ctypes
# Test ctypes.CField
import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField)]

x = X()
y = Y()

x.a = 1
x.b = 2

y.a = 1
y.b = x

print(x.a, x.b)
print(y.a, y.b.a, y.b.b)

# Test ctypes.Structure.from_address
import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

x = X()
x.a = 1
x.b = 2

x2 = ctypes.Structure.from_address(ctypes.addressof(x))
print(x2.
