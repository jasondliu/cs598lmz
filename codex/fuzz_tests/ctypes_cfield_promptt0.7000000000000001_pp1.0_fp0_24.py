import ctypes
# Test ctypes.CField
class C:
    _fields_ = [('i', ctypes.c_int)]
    
C._fields_ = [('j', ctypes.c_int)]

a = C()
a.j = 1
print(a.i)
print(a.j)

# Test ctypes.CField
class D(ctypes.Structure):
    _fields_ = [('i', ctypes.c_int)]
    
D._fields_ = [('j', ctypes.c_int)]

a = D()
a.j = 1
print(a.i)
print(a.j)

# Test NamedField
class C:
    _fields_ = [('i', ctypes.c_int)]
    
C.j = ctypes.c_int

a = C()
a.j = 1
print(a.i)
print(a.j)

# Test NamedField
class D(ctypes.Structure):
    _fields_ = [('i', ctypes.c_int)]
    
D.j = ctypes.
