import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.CField, 24),
                ('b', ctypes.CField, 8)]

class Y(X):
    _fields_ = X._fields_ + [('c', ctypes.CField, 8)]

class Z(X):
    _fields_ = X._fields_ + [('d', ctypes.CField, 8)]

x = X()
print ctypes.sizeof(x)

y = Y()
print ctypes.sizeof(y)

z = Z()
print ctypes.sizeof(z)
