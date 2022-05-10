import ctypes

class S(ctypes.Structure):
    x = 42
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
        ("d", ctypes.c_int),
    ]


p = ctypes.create_string_buffer(ctypes.sizeof(S))

s = ctypes.cast(ctypes.pointer(p), ctypes.POINTER(S)).contents

s.a = 1
s.b = 2
s.c = 3
s.d = 4

print(s)

b = bytes(p)
print(b)

