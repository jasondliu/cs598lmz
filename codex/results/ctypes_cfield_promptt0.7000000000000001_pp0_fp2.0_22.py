import ctypes
# Test ctypes.CField

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class B(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.POINTER(A)),
                ("d", ctypes.POINTER(B))]

print A.b
print B.b
print C.a
print C.b
print C.c
print C.d

print type(A.b)
print type(B.b)
print type(C.a)
print type(C.b)
print type(C.c)
print type(C.d)
