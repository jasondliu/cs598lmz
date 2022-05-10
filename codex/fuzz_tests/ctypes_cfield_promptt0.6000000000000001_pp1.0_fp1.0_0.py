import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

obj = Z()
obj.y.x.y = 5

print("obj.y.x.y =", obj.y.x.y)

obj.y.x = X(1, 2)

print("obj.y.x.y =", obj.y.x.y)

obj.y.x = Y(1, 2, X(3, 4))

print("obj.y.x.y =", obj.y.x.y)

obj.y.x = Z(Y(1, 2, X(3, 4
