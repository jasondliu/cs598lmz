import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32
    y = ctypes.c_int32

s = S.from_address(0x80000000)
s.x = 1  # Causes segfault on 32 bit
s.y = 2  # Causes segfault on 32 bit
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
s.x = 1
s.y = 2
