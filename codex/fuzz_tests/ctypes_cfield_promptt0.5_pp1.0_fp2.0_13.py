import ctypes
# Test ctypes.CField
class Struct(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Struct2(ctypes.Structure):
    _fields_ = [("s", Struct),
                ("c", ctypes.c_char)]

s = Struct2()
s.s.a = 1
s.s.b = 2
s.c = 'x'

print(s.s.a, s.s.b, s.c)

# Test ctypes.CArray
class Struct3(ctypes.Structure):
    _fields_ = [("array", ctypes.c_int * 3)]

s = Struct3()
s.array[0] = 1
s.array[1] = 2
s.array[2] = 3

print(s.array[0], s.array[1], s.array[2])

# Test ctypes.CArray with nested structure
class Struct4(ctypes.Structure):
    _fields_ = [("array", Struct *
