import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3
print(s.x, s.y, s.z)

ss = ctypes.cast(ctypes.pointer(s), ctypes.POINTER(ctypes.c_int))

print(ss[0], ss[1], ss[2])

ss[0] = 4
ss[1] = 5
ss[2] = 6
print(ss[0], ss[1], ss[2])

print(s.x, s.y, s.z)
