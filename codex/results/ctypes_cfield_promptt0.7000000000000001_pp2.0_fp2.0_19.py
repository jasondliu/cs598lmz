import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField)]
    def __init__(self):
        self.b = 42

x = X()
print(x.a)
print(x.b)

class Y(X):
    _fields_ = X._fields_ +[("c", ctypes.c_char)]

y = Y()
print(y.a)
print(y.b)
print(y.c)
y.c = b'X'
print(y.c)

# Test ctypes.Field
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.Field(ctypes.c_char, offset=1))]
    def __init__(self):
        self.a = 42

z = Z()
print(z.a)
print(z.b)
z.b = b'X'
print(z.a)
