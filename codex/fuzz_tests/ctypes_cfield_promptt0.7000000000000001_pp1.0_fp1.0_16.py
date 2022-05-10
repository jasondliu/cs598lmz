import ctypes
# Test ctypes.CFields


class Test(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
    ]

t = Test()
print(t.x)
print(t.y)
print(t.z)
print(t.a)
print(t.b)
print(t.c)

t.x = 1
t.y = 2
t.z = 3

print(t.x)
print(t.y)
print(t.z)
print(t.a)
print(t.b)
print(t.c)

# Test ctypes.CFields vs ctypes.Fields

dt = ctypes.DataType('Test2', (ctypes.Structure,), {})
flds = [
        ('x', ctypes
