import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [
        ("a", ctypes.c_char_p),
        ("b", ctypes.c_char_p),
    ]

print(S.x)
print(S.a)
print(S.b)
print(S.x)
