import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

y = Y()
print y.x.a, y.x.b
y.x.a = 1
y.x.b = 2
print y.x.a, y.x.b
print y.y
y.y = 3
print y.y

# Test ctypes.CField.from_address

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class W(ctypes.Structure):
    _fields_ = [("x", Z),
                ("y", ctypes.c_int)]

w = W()
w.y = 3
print w.y

z = ctypes.CField.from_
