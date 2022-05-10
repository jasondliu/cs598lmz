import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

X.x.__class__

# Test ctypes.Field
class Y(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

Y.x.__class__

# Test ctypes.Structure.from_address
class Z(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

z = Z()
z.x = 1
Z.from_address(ctypes.addressof(z)).x


# Test ctypes.addressof
class A(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

a = A()
a.x = 1
ctypes.addressof(a)


# Test ctypes.byref
class B(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

b = B()
b.x = 1
