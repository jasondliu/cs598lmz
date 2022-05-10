import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long
    y = ctypes.c_long

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)
print(s)

print(ctypes.sizeof(S))
print(ctypes.sizeof(s))

print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
print(ctypes.addressof(s.y))

print(ctypes.cast(ctypes.addressof(s), ctypes.POINTER(S)))
print(ctypes.cast(ctypes.addressof(s.x), ctypes.POINTER(S)))
print(ctypes.cast(ctypes.addressof(s.y), ctypes.POINTER(S)))

print(ctypes.cast(ctypes.addressof(s), ctypes.POINTER(S)).contents)
print(ctypes.cast(ctypes.addressof(s.x), ctypes.POINTER(S)).contents)

