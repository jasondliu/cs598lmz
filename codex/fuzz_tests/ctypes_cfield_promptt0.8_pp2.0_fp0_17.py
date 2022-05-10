import ctypes
# Test ctypes.CField
class Point2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

Point3 = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.POINTER(Point2), ctypes.c_int )

pt = Point2(11, 22)
pf = Point3(_t1.point3)

print(pf(pt, 2))

# Test ctypes.CFUNCTYPE

def adder(a, b):
    return a + b

a = ctypes.c_int.in_dll(_t1, "a")
b = ctypes.c_int.in_dll(_t1, "b")

add = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(_t1.add)

print(add(a.value, b.value))

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes
