import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    c = ctypes.CField(ctypes.c_int, X, "a")
    d = ctypes.CField(ctypes.c_int, X, "b")

x = X()
x.a = 1
x.b = 2
assert x.c == 1
assert x.d == 2

# Test ctypes.CField.from_address
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    c = ctypes.CField.from_address(ctypes.addressof(Y), "a")
    d = ctypes.CField.from_address(ctypes.addressof(Y), "b")

y = Y()
y.a = 1
y.b = 2
assert y.c == 1
assert y.d == 2

# Test c
