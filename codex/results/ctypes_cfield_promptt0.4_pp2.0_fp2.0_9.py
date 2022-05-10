import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["b"]

print(X.a)
print(X.b)
print(X.__dict__['a'])
print(X.__dict__['b'])
print(X._fields_)
print(X._anonymous_)

# Test ctypes.CField.from_address
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["b"]

y = Y()
print(y.a)
print(y.b)
print(y.__dict__['a'])
print(y.__dict__['b'])
print(y._fields_)
print(y._anonymous_)

# Test ctypes.CField.from_param
class Z(ctypes.Structure):
    _fields_
