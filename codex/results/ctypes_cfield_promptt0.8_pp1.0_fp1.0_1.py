import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
	_fields_ = [("d", ctypes.c_int)]

a = A()
print(a.d)
a.d = 2
print(a.d)
