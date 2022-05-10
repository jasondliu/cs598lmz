import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()
print(s.x)
print(s.y)

# s.x = 7
# print(s.x)

ss = ctypes.pointer(s)
ss.contents.x = 7
print(s.x)

# print(ss.contents.x)
