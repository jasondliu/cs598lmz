import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [("d", D),
                ("e", ctypes.c_int)]

e = E()
e.d.c.a = 1
e.d.c.b = 2
e.d.d = 3
e.e = 4

print e.d.c.a, e.d.c.b, e.d.d, e.e

# Test ctypes.CArray
array_type = ctypes.c_int * 3

array = array_type()
array[0] = 1
array[1] = 2
array[2] = 3

for i in array:
    print i

# Test ctypes.CFuncPtr
def func(a, b
