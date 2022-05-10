import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("a", ctypes.c_int)]

class W(ctypes.Structure):
    _fields_ = [("z", Z),
                ("a", ctypes.c_int)]

# Test ctypes.CField.from_address()
w = W()
w.a = 1
w.z.y.x.a = 2
w.z.y.x.b = 3
w.z.a = 4

a = ctypes.c_int.from_address(ctypes.addressof(w.z.y.x.a))
b = ctypes.c_int.from_address(ctypes.addressof(w.z.y.x.b))
c =
