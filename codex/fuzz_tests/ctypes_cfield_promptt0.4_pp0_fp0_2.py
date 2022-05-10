import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]
    _anonymous_ = [('b', ctypes.c_int)]
    _anonymous_ = [('c', ctypes.c_int)]
    _fields_ = [('d', ctypes.c_int)]

# Test ctypes.CField.from_address()
class D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]
    _anonymous_ = [('b', ctypes.c_int)]
    _anonymous_ = [('c', ctypes.c_int)]
    _fields_ = [('d', ctypes.c_int)]

d = D()
d.a = 1
d.b = 2
d.c = 3
d.d = 4

print(ctypes.CField.from_address(ctypes.addressof(d), D, 'a'))
print(ctypes.CField.from_address(ctypes.addressof(d), D
