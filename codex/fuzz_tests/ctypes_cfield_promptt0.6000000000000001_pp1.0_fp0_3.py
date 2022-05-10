import ctypes
# Test ctypes.CField
class Struct(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_long),
        ('z', ctypes.c_double)]

obj = Struct()
obj.x = 1
obj.y = 2
obj.z = 3.0

print(obj.x, obj.y, obj.z)
print(obj)
print(ctypes.sizeof(obj))
print(ctypes.sizeof(ctypes.c_int))
print(ctypes.sizeof(ctypes.c_long))
print(ctypes.sizeof(ctypes.c_double))

class Struct2(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_long),
        ('z', ctypes.c_double),
        ('w', ctypes.c_int)]

obj2 = Struct2()
obj2.x = 1
obj2.y = 2
obj2.z = 3.
