import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
A.x.__doc__ = "A.x"
a = A()
print(a.x.__doc__)
