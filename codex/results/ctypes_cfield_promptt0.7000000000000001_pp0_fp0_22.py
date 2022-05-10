import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int)]

class D(C):
    i = ctypes.CField("i")
d = D()
d.i = 1
print(d.i)
x = d.i
print(x)
# Test ctypes.Field
class E(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int)]

class F(E):
    i = ctypes.Field("i")
f = F()
f.i = 1
print(f.i)
y = f.i
print(y)
