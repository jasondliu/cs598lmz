import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [("a", ctypes.POINTER(POINT)),
                ("b", ctypes.POINTER(POINT))]

p = POINT()
p.x = 1
p.y = 2

r = RECT()
r.a = ctypes.pointer(p)
r.b = ctypes.pointer(p)

print r.a.contents.x
print r.b.contents.y
# Test ctypes.c_char_p
import ctypes
libc = ctypes.CDLL("libc.so.6")
print libc.strdup("hello")
# Test ctypes.c_void_p
import ctypes
libc = ctypes.CDLL("libc.so.6")
print libc.malloc(1)
# Test ctypes.c_void_p.from_
