import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ushort
    y = ctypes.c_ushort
    z = ctypes.c_ushort

val = ctypes.c_ushort(0x1234)
s = S()
s.x = val
s.y = val
s.z = val
