import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int, 1),
                ("z", ctypes.c_int, 2)]

print C.x
print C.y
print C.z
print C.y.offset
print C.z.offset
print C.y.size
print C.z.size
print C.y.index
print C.z.index
print C.y.bitsize
print C.z.bitsize

# Test ctypes.Field
class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int, 1),
                ("z", ctypes.c_int, 2)]

print C.x
print C.y
print C.z
print C.y.offset
print C.z.offset
print C.y.size
print C.z.size
print C.y.index
print C.z.index
print C.y.
