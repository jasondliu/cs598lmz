import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int, 4),
                ("c", ctypes.c_int, 4),
                ("d", ctypes.c_int, 4),
                ("e", ctypes.c_int),
                ("f", ctypes.c_int),
                ("g", ctypes.c_int),
                ("h", ctypes.c_int),
                ("i", ctypes.c_int),
                ("j", ctypes.c_int)]

c = C()
print(c.b)
print(c.c)
print(c.d)
print(c.e)
print(c.f)
print(c.g)
print(c.h)
print(c.i)
print(c.j)

c.a = 0xffffffff
c.b = 0xffffffff
c.c = 0xffffffff
c.d = 0xffffffff
c.e = 0xffffffff
