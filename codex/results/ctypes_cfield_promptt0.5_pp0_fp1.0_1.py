import ctypes
# Test ctypes.CField.
import ctypes._testcapi

# Test that the fields in a structure are properly initialized.
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

x = X()
print x.a, x.b

# Test that the fields in a structure are properly initialized.
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

y = Y(1, 2)
print y.a, y.b

# Test that the fields in a structure are properly initialized.
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

z = Z(b=2, a=1)
print z.a, z.b

# Test that the fields in a structure are properly initialized.
class W(ctypes.Structure):
    _fields_ = [
