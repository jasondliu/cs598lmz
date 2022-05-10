import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

class D(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

class C(ctypes.Structure):
    _fields_ = [("s", S), ("d", D)]

class C2(ctypes.Structure):
    _fields_ = [("s", S), ("d", D)]

class C3(ctypes.Structure):
    _fields_ = [("s", S), ("d", D)]

print C.s.x
print C.d.y

print C.s.offset
print C.d.offset

print ctypes.sizeof(C)

C.s.x = ctypes.c_int(3)
C.d.y = ctypes.c_int(4)

print C.s.x
print C.d.y

print C.s.offset
print C.d.offset

print ctypes.sizeof(C)

C
