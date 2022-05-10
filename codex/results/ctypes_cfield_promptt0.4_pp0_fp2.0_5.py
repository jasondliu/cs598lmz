import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

# Test ctypes.CField.from_address
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

y = Y()
y.a = 42
y_a = ctypes.CField.from_address(ctypes.addressof(y), "a")

# Test ctypes.CField.from_param
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

z = Z()
z.a = 42
z_a = ctypes.CField.from_param(z.a)

# Test ctypes.CField.from_buffer
class W(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

w = W()
w.a = 42
w_a = ctypes.CField.from_buffer(w, "a")

# Test ctypes.
