import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

    _pack_ = 1
    _fields_ = [
        ("byte", ctypes.c_uint8),
        ("long", ctypes.c_longlong),
        ("int", ctypes.c_int),
        ("nest1", ("int", 4)),
        ("byte2", ctypes.c_uint8),
    ]

print(S.x)
print(S.x.real)
print(S.x + 30)
print(S.x.real + 30)

a = S.x + 30
print(a.value == 33)
print(a.real.value == 33)


print(S.byte)
print(S.byte.real)
print(S.byte + 30)
print(S.byte.real + 30)

a = S.byte + 30
print(a.value == 34)
print(a.real.value == 34)

print(S.nest1)
print(S.nest1.real)
print(S.nest1 + 30)
print(S
