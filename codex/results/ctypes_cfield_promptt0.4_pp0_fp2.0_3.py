import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C)]

obj = D()
obj.c.a = 1
obj.c.b = 2

print(obj.c.a, obj.c.b)

obj.c = C(3, 4)

print(obj.c.a, obj.c.b)
