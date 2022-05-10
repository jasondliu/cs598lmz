import ctypes
# Test ctypes.CField instance

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_int),
                ("f", ctypes.c_int),
                ("g", ctypes.c_int),
                ("h", ctypes.c_int),
                ("i", ctypes.c_int),
                ("j", ctypes.c_int)]

print C.a
print C.b
print C.c
print C.d
print C.e
print C.f
print C.g
print C.h
print C.i
print C.j

print C.a.offset
print C.b.offset
print C.c.offset
print C.d.offset
print C.e.offset
print C.f.offset
print C.g.offset
print C.h.offset
print C.i.offset
print C.
