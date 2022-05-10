import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char_p),
                ("c", ctypes.c_char_p)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("d", ctypes.c_char_p)]

x = X()
x.a = 1
x.b = "hello"
x.c = "world"

y = Y()
y.x = x
y.d = "!"

print(y.x.a, y.x.b, y.x.c, y.d)

# Test ctypes.CField
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char_p),
                ("c", ctypes.c_char_p)]

class W(ctypes.Structure):
    _fields_ = [("x", Z),
                ("d
