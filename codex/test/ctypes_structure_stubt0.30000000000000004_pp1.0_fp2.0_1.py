import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class A(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int),
                ("s", S)]

class B(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int),
                ("s", S)]

a = A()
b = B()

a.y = 1
a.s.x = 2

b.y = 3
b.s.x = 4

print(a.y, a.s.x)
print(b.y, b.s.x)

a.s = b.s

print(a.y, a.s.x)
print(b.y, b.s.x)

b.s.x = 5

print(a.y, a.s.x)
print(b.y, b.s.x)
