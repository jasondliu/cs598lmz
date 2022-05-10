import ctypes

class S(ctypes.Structure):
    x = 1
    y = x + 1
    z = x + 2
    w = y + z
    _fields_ = [("a", ctypes.c_int, y),
                ("b", ctypes.c_int, z),
                ("c", ctypes.c_int, w),
                ("d", ctypes.c_int, x)]

print(S.x, S.y, S.z, S.w)
print(S.d, S.a, S.b, S.c)
