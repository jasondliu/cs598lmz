import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

obj = Z()
obj.y.x.a = 1
obj.y.x.b = 2
obj.y.y = 3
obj.z = 4

print(obj.y.x.a)
print(obj.y.x.b)
print(obj.y.y)
print(obj.z)

# Test ctypes.CArray
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x
