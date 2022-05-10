import ctypes
# Test ctypes.CField

class Struct(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Test(ctypes.Structure):
    _fields_ = [("s", Struct)]

class Test2(ctypes.Structure):
    _fields_ = [("s", ctypes.CField(Struct))]

t = Test()
t.s.a = 1
t.s.b = 2

t2 = Test2()
t2.s.a = 1
t2.s.b = 2

print(t.s.a, t.s.b)
print(t2.s.a, t2.s.b)
