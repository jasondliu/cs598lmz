import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16(1)
    y = ctypes.c_int16(2)

s = S()
s.x = s.x & s.y
s.x = s.x | s.y
s.x = s.x ^ s.y
s.x = s.x & ctypes.c_int16(1)
s.x = s.x | ctypes.c_int16(1)
s.x = s.x ^ ctypes.c_int16(1)
s.x = s.x & ctypes.c_int16
s.x = s.x | ctypes.c_int16
s.x = s.x ^ ctypes.c_int16
s.x = s.x & ctypes.c_int16(1).value
s.x = s.x | ctypes.c_int16(1).value
s.x = s.x ^ ctypes.c_int16(1).value
s.x = ctypes.c_int16(1) & s.y
s.x =
