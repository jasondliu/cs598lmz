import ctypes
# Test ctypes.CField
class Struct(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField)]

s = Struct()
print(s.a)
s.a = 2
print(s.a)

# Test ctypes.CField with a structure
class Struct2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", Struct)]

s2 = Struct2()
print(s2.a)
print(s2.c.a)
s2.c.a = 3
print(s2.c.a)

# Test ctypes.CField with a union
class Union(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

class Struct3(ctypes.Structure):
   
