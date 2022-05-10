import ctypes
# Test ctypes.CField with struct module

# This test should pass if the ctypes module is compiled with gcc,
# otherwise it will fail (see issue #10345)

POINT = struct.Struct("x y")
class POINT(ctypes.Structure):
    _fields_ = (
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
    )

print(type(POINT.x))
print(type(POINT.y))
print(type(POINT._fields_[0][1]))
print(type(POINT._fields_[1][1]))
print(type(POINT.x) is type(POINT._fields_[0][1]))
print(type(POINT.y) is type(POINT._fields_[1][1]))
