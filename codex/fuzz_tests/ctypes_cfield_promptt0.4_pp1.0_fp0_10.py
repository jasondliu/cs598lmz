import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

y = Y()
y.x.a = 42
y.x.b = 43
y.c = 44

print y.x.a, y.x.b, y.c
print y.x

# Test ctypes.CField.from_param
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

def test(z):
    print z.a, z.b

test(Z(42, 43))

# Test ctypes.CField.from_address
class T(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
