import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte
    y = ctypes.c_short
    z = ctypes.c_int

ctypes.memmove(ctypes.addressof(S())+ctypes.sizeof(S.x), ctypes.addressof(S())+ctypes.sizeof(S.y), ctypes.sizeof(S.y))
# s = S()
# memmove(ctypes.addressof(s)
# print(s.x, s.y, s.z)
