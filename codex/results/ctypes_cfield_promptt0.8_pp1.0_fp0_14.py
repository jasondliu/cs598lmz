import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [('_x', ctypes.c_int), ('_y', ctypes.c_short)]
    x = ctypes.CField(('_x', ctypes.c_int), (1, 0))
    y = ctypes.CField(('_y', ctypes.c_short), (1, 2))

a = A()
a.x = 0x12345678
a.y = 0x1234
print hex(a._x), hex(a._y)
a._x = 0xffffffff
a._y = 0xffff
print hex(a.x), hex(a.y)

# Test ctypes.Field
class B(ctypes.Structure):
    _fields_ = [('_x', ctypes.c_int), ('_y', ctypes.c_short)]
    x = ctypes.Field(('_x', ctypes.c_int), (1, 0))
    y = ctypes.Field(('_y', ctypes.c_short), (1,
