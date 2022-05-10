import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class A(ctypes.Structure):
    _fields_ = [("a", S),
                ("b", S)]

class B(ctypes.Structure):
    _fields_ = [("b", S),
                ("a", S)]

print(A.a.offset)
print(A.b.offset)

print(B.a.offset)
print(B.b.offset)
