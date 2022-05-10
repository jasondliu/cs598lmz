import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

x = X()
x.a = 1
x.b = 2
print(x.a, x.b)

x_pointer = ctypes.pointer(x)
print(x_pointer.contents)

# Test ctypes.Field
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

y = Y()
y.a = 1
y.b = 2
print(y.a, y.b)

y_pointer = ctypes.pointer(y)
print(y_pointer.contents)

# Test ctypes.Array
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int * 2)]

z = Z()
z.a = (1, 2)
print(z.a[0], z.a[
