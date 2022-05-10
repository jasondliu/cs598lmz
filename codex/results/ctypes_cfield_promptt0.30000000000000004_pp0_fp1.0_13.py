import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

# Test ctypes.CField.__get__
y = Y()
y.x.a = 1
y.x.b = 2
y.y = 3
print(y.x.a, y.x.b, y.y)

# Test ctypes.CField.__set__
y.x.a = 4
y.x.b = 5
y.y = 6
print(y.x.a, y.x.b, y.y)

# Test ctypes.CField.__delete__
del y.x.a
del y.x.b
del y.y
print(y.x.a, y.x.b, y.y)
